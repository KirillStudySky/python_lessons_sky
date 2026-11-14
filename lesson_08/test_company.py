import pytest
import uuid


def test_create_project_positive(api_client):
    #Позитивный тест: Успешное создание проекта
    unique_title = f"Project_{uuid.uuid4().hex[:6]}"
    response = api_client.create_project(title=unique_title)

    # Проверяем статус и наличие ID в ответе на создание
    assert response.status_code in (200, 201)
    res_data = response.json()
    assert "id" in res_data

    # Дополнительно проверяем через GET-запрос, что название сохранилось корректно
    project_id = res_data["id"]
    get_response = api_client.get_project(project_id=project_id)
    assert get_response.status_code == 200
    assert get_response.json().get("title") == unique_title


def test_create_project_negative_empty_title(api_client):
    #Негативный тест: Создание проекта с пустым названием
    response = api_client.create_project(title="")

    # Ожидаем код ошибки (зависит от логики API Yougile, обычно 400 Bad Request)
    assert response.status_code == 400


def test_get_project_positive(api_client, clean_project):
    #Позитивный тест: Получение существующего проекта по ID
    project_id = clean_project
    response = api_client.get_project(project_id=project_id)

    assert response.status_code == 200
    assert response.json().get("id") == project_id


def test_get_project_negative_invalid_token(api_client, clean_project):
    #Негативный тест: Получение проекта с невалидным токеном авторизации
    project_id = clean_project
    invalid_headers = {"Authorization": "Bearer invalid_token_123"}

    response = api_client.get_project(project_id=project_id, headers=invalid_headers)

    # Ожидаем ошибку авторизации
    assert response.status_code in [401, 403]


def test_update_project_positive(api_client, clean_project):
    #Позитивный тест: Успешное обновление названия проекта
    project_id = clean_project
    new_title = "Updated Project Title"

    response = api_client.update_project(project_id=project_id, title=new_title)

    assert response.status_code == 200

    # Проверяем через GET, что данные действительно изменились
    get_response = api_client.get_project(project_id=project_id)
    assert get_response.json().get("title") == new_title


def test_update_project_negative_non_existent_id(api_client):
    #Негативный тест: Обновление проекта с несуществующим ID
    non_existent_id = "00000000-0000-0000-0000-000000000000"

    response = api_client.update_project(project_id=non_existent_id, title="New Title")

    # Ожидаем код 404 Not Found
    assert response.status_code == 404
