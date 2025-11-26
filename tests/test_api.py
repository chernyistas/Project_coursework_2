import pytest
from src.api import HeadHunterAPI
from typing import Any

def test_connect_success(monkeypatch: Any, mock_response_ok: Any) -> None:
    """Тест на успешное подключение"""

    api = HeadHunterAPI()
    monkeypatch.setattr(api, "_HeadHunterAPI__BASE_URL", "https://test.ru")
    monkeypatch.setattr("requests.get", lambda *args, **kwargs: mock_response_ok)
    response = api._connect()
    assert response.status_code == 200

def test_connect_fail(monkeypatch: Any, mock_response_fail: Any) -> None:
    """Тест на ошибку при подключении"""

    api = HeadHunterAPI()
    monkeypatch.setattr(api, "_HeadHunterAPI__BASE_URL", "https://test.ru")
    monkeypatch.setattr("requests.get", lambda *args, **kwargs: mock_response_fail)
    with pytest.raises(ConnectionError):
        api._connect()

def test_get_vacancies(monkeypatch: Any, mock_response_ok: Any) -> None:
    """Тест на получение вакансий"""
    monkeypatch.setattr("requests.get", lambda url, params=None: mock_response_ok)
    api = HeadHunterAPI()
    vacancies = api.get_vacancies("python")
    assert isinstance(vacancies, list)
    assert vacancies[0]["name"] == "Python Developer"