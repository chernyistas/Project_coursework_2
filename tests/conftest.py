from typing import Any, Dict, List

import pytest

from src.vacancy import Vacancy


class MockResponseOK:
    """Mock-объект для успешного ответа request.get"""

    status_code: int = 200

    def json(self) -> dict:
        return {
            "items": [
                {
                    "name": "Python Developer",
                    "alternate_url": "test_url",
                    "salary": None,
                    "snippet": {"requirement": "desk"},
                }
            ]
        }


class MockResponseFail:
    """Mock-объект для неуспешного ответа request.get"""

    status_code: int = 500

    def json(selfself) -> dict:
        return {}


@pytest.fixture
def mock_response_ok() -> MockResponseOK:
    """Фикстура успешного mock-ответа"""
    return MockResponseOK()


@pytest.fixture()
def mock_response_fail() -> MockResponseFail:
    """Фикстура неуспешного mock-ответа"""
    return MockResponseFail()


@pytest.fixture
def sample_json() -> List[Dict[str, Any]]:
    """Фикстура JSON списка словарей"""
    return [
        {
            "name": "Developer",
            "alternate_url": "url",
            "salary": {"from": 100000, "to": 200000, "currency": "RUR"},
            "snippet": {"requirement": "desc"},
        }
    ]


@pytest.fixture
def vac_1() -> Vacancy:
    """Фикстура вакансии"""
    return Vacancy("Developer", "url", None, "description")


@pytest.fixture
def vac_2() -> Vacancy:
    """Фикстура вакансии"""
    return Vacancy("Python Dev", "url", "100000", "description")


@pytest.fixture
def vac_3() -> Vacancy:
    """Фикстура вакансии"""
    return Vacancy("Worker", "url", "200000", "description")


@pytest.fixture
def vac_4() -> Vacancy:
    """Фикстура вакансии"""
    return Vacancy("Java Dev", "url", "100000", "description")


@pytest.fixture
def sample_vacancies() -> List[Vacancy]:
    """Фикстура списка вакансий"""
    return [
        Vacancy("Python Dev", "url1", "150000", "description Python"),
        Vacancy("Worker", "url2", "100000", "description Worker"),
        Vacancy("Java Dev", "url3", "0", "description Java"),
    ]


@pytest.fixture
def vacancy() -> List[Vacancy]:
    """Фикстура описания вакансии с тегами"""
    return [
        Vacancy(
            "Разработчик <highlighttext>Python</highlighttext>",
            "http://anywhere",
            "150000",
            "Требования: <highlighttext>FastAPI</highlighttext> опыт",
        )
    ]
