from typing import Any, Dict, List

from src.vacancy import Vacancy


def test_salary_validation(vac_1: Vacancy, vac_2: Vacancy) -> None:
    """Проверяет валидацию зарплаты при создании вакансий"""

    assert vac_1.salary == "Зарплата не указана"
    assert Vacancy._salary_value("Зарплата не указана") == 0
    assert vac_2.salary == "100000"
    assert Vacancy._salary_value("100000") == 100000


def test_comparisons(vac_2: Vacancy, vac_3: Vacancy, vac_4: Vacancy) -> None:
    """Проверяет работу операторов сравнения между вакансиями по зарплате"""

    assert vac_2 < vac_3
    assert vac_3 > vac_4
    assert vac_2 == vac_4


def test_cast_to_object_list(sample_json: List[Dict[str, Any]]) -> None:
    """Тест на преобразование данных из JSON (словарей) в список объектов Vacancy"""

    vacancies: List[Vacancy] = Vacancy.cast_to_object_list(sample_json)
    assert len(vacancies) == 1
    assert vacancies[0].name == "Developer"
    assert "от 100000" in vacancies[0].salary or "100000" in vacancies[0].salary
