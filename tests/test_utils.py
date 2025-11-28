from typing import List

import pytest

from src.utils import (clean_highlight_tags, filter_vacancies, get_top_vacancies, get_vacancies_by_salary,
                       print_vacancies, sort_vacancies)
from src.vacancy import Vacancy


def test_filter_vacancies(sample_vacancies: List[Vacancy]) -> None:
    """Тест на фильтрацию вакансий по ключевому слову"""

    filtered: List[Vacancy] = filter_vacancies(sample_vacancies, ["python"])
    assert len(filtered) == 1
    assert filtered[0].name == "Python Dev"


def test_get_vacancies_by_salary(sample_vacancies: List[Vacancy]) -> None:
    """Тест фильтрации по диапазону зарплаты"""

    ranged: List[Vacancy] = get_vacancies_by_salary(sample_vacancies, "120000-160000")
    assert len(ranged) == 1
    assert ranged[0].salary == "150000"


def test_sort_and_top_vacancies(sample_vacancies: List[Vacancy]) -> None:
    """Тест на сортировку вакансий по зарплате"""

    sorted_v: List[Vacancy] = sort_vacancies(sample_vacancies)
    assert sorted_v[0].salary == "150000"
    top_two: List[Vacancy] = get_top_vacancies(sorted_v, 2)
    assert len(top_two) == 2


def test_clean_highlight_tags_removes_tags() -> None:
    """Тест на удаление тегов"""

    text = "Это <highlighttext>Python</highlighttext> и <highlighttext>FastAPI</highlighttext>."
    cleaned = clean_highlight_tags(text)
    assert cleaned == "Это Python и FastAPI."


def test_clean_highlight_tags_without_tags() -> None:
    """Тест на не изменение строки без тегов"""

    text = "Это просто текст."
    cleaned = clean_highlight_tags(text)
    assert cleaned == text


def test_clean_highlight_tags_partial_tag() -> None:
    """Тест на работу с одним тегом"""

    text = "Только <highlighttext>Python</highlighttext>."
    cleaned = clean_highlight_tags(text)
    assert cleaned == "Только Python."


def test_print_vacancies_removes_tags(vacancy: List[Vacancy], capsys: pytest.CaptureFixture) -> None:
    """Тест на печать описания без тегов"""

    print_vacancies(vacancy)
    out = capsys.readouterr().out
    assert "<highlighttext>" not in out
    assert "Python" in out
    assert "FastAPI" in out
    assert "Разработчик Python" in out
    assert "Требования: FastAPI опыт" in out
