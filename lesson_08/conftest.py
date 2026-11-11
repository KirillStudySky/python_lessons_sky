import pytest
from CompanyHelper import CompanyHelp

BASE_URL = "https://yougile.com"
TOKEN = "cksadG32fmjc5GFvs-2z1sIBQcEZ1yKXCJMzvbSRxb8fDsIFU9mKAiLkSZFlkDy1"


@pytest.fixture(scope="session")
def api_client():
    #Инициализация API клиента для всей сессии тестов
    return CompanyHelp(base_url=BASE_URL, token=TOKEN)


@pytest.fixture
def clean_project(api_client):
    #Фикстура для создания временного проекта.
    # Предусловие: создаем проект
    response = api_client.create_project(title="Test Project for Fixture")
    project_id = response.json().get("id")

    yield project_id
