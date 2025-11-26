import pytest
from typing import Any

class MockResponseOK:
    """Mock-объект для успешного ответа request.get"""

    status_code: int = 200
    def json(self) -> dict:
        return {
            "items":[
                {
                    "name": "Python Developer",
                    "alternate_url": "test_url",
                    "salary": None,
                    "snippet": {"requirement": "desk"}
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
