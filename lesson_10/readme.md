# Автотесты с Allure отчетами

Проект содержит автотесты с использованием Page Object и Allure отчетов.

## Запуск тестов

```bash
# Установка
pip install selenium pytest allure-pytest

# Запуск всех тестов
pytest --alluredir=allure-results

# Запуск теста калькулятора
pytest calculator/calculator_test.py --alluredir=allure-results

# Запуск теста магазина
pytest shop/test_shop.py --alluredir=allure-results

# Открытие Сайта Allure с выполненными тестами
allure serve allure-results
