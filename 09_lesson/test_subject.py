import pytest
from database import Database

db_connection = "postgresql://postgres:161Alex322@localhost:5432/QA"


@pytest.fixture
def db():
    return Database(db_connection)


def get_max_id(db):
    result = db.execute_query("SELECT MAX(subject_id) FROM subject")
    return result[0][0]


def test_add_subject(db):
    max_id = get_max_id(db)
    new_id = max_id + 1

    db.execute_query(
        "INSERT INTO subject (subject_id, subject_title) VALUES (:id, :title)",
        {"id": new_id, "title": "Тестирование ПО"}
    )

    rows = db.execute_query(
        "SELECT * FROM subject WHERE subject_id = :id", {"id": new_id})
    assert len(rows) == 1
    assert rows[0][1] == "Тестирование ПО"

    db.execute_query(
        "DELETE FROM subject WHERE subject_id = :id", {"id": new_id})


def test_update_subject(db):
    max_id = get_max_id(db)
    new_id = max_id + 1

    db.execute_query(
        "INSERT INTO subject (subject_id, subject_title) VALUES (:id, :title)",
        {"id": new_id, "title": "Программирование"}
    )

    db.execute_query(
        "UPDATE subject SET subject_title = :title WHERE subject_id = :id",
        {"title": "Разработка", "id": new_id}
    )

    rows = db.execute_query(
        "SELECT * FROM subject WHERE subject_id = :id", {"id": new_id})
    assert len(rows) == 1
    assert rows[0][1] == "Разработка"

    db.execute_query(
        "DELETE FROM subject WHERE subject_id = :id", {"id": new_id})


def test_delete_subject(db):
    max_id = get_max_id(db)
    new_id = max_id + 1

    db.execute_query(
        "INSERT INTO subject (subject_id, subject_title) VALUES (:id, :title)",
        {"id": new_id, "title": "Базы данных"}
    )

    rows_before = db.execute_query(
        "SELECT * FROM subject WHERE subject_id = :id", {"id": new_id})
    assert len(rows_before) == 1

    db.execute_query(
        "DELETE FROM subject WHERE subject_id = :id", {"id": new_id})

    rows_after = db.execute_query(
        "SELECT * FROM subject WHERE subject_id = :id", {"id": new_id})
    assert len(rows_after) == 0
