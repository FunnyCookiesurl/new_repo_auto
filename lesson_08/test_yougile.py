import requests
from config import bases_url, api_token

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_token}"
}


def create_project(title, description=None):
    data = {"title": title}
    if description:
        data["description"] = description
    response = requests.post(
        f"{bases_url}/projects",
        headers=headers,
        json=data
    )
    return response


def get_project(project_id):
    response = requests.get(
        f"{bases_url}/projects/{project_id}",
        headers=headers
    )
    return response


def update_project(project_id, new_title):
    data = {"title": new_title}
    response = requests.put(
        f"{bases_url}/projects/{project_id}",
        headers=headers,
        json=data
    )
    return response


def test_api_connection():
    response = requests.get(
        f"{bases_url}/projects",
        headers=headers
    )
    assert response.status_code != 401


def test_create_project_positive():
    response = create_project("Мой новый проект")
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    project_id = data["id"]
    get_response = get_project(project_id)
    assert get_response.status_code == 200
    project_data = get_response.json()
    assert project_data["title"] == "Мой новый проект"


def test_create_project_negative_no_title():
    response = create_project("")
    assert response.status_code == 400


def test_get_project_positive():
    response = create_project("Проект для получения")
    project_id = response.json()["id"]
    response = get_project(project_id)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == project_id
    assert data["title"] == "Проект для получения"


def test_get_project_negative():
    response = get_project("несуществующий-id-123")
    assert response.status_code == 404


def test_update_project_positive():
    response = create_project("Старое название")
    project_id = response.json()["id"]
    response = update_project(project_id, "Новое название")
    assert response.status_code == 200
    get_response = get_project(project_id)
    project_data = get_response.json()
    assert project_data["title"] == "Новое название"


def test_update_project_negative():
    response = update_project("несуществующий-id-456", "Любое название")
    assert response.status_code == 404
