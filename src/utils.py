import re
from typing import List

from src.vacancy import Vacancy


def filter_vacancies(vacancies: List[Vacancy], keywords: List[str]) -> List[Vacancy]:
    """Фильтрует вакансии по ключевым словам"""

    return [v for v in vacancies if all(kw.lower() in (v.name + v.description).lower() for kw in keywords)]


def get_vacancies_by_salary(vacancies: List[Vacancy], salary_range: str) -> List[Vacancy]:
    """Фильтрация вакансий по диапазону зарплат"""
    try:
        min_salary, max_salary = map(int, salary_range.split("-"))
    except Exception:
        return vacancies
    return [v for v in vacancies if min_salary <= Vacancy._salary_value(v.salary) <= max_salary]


def sort_vacancies(vacancies: List[Vacancy]) -> List[Vacancy]:
    """Сортирует вакансии по зарплате по убыванию"""

    return sorted(vacancies, reverse=True)


def get_top_vacancies(vacancies: List[Vacancy], top_n: int) -> List[Vacancy]:
    """Метод берёт первые N вакансий"""

    return vacancies[:top_n]


def clean_highlight_tags(text: str) -> str:
    """Метод удаляет теги из текста"""
    return re.sub(r"<highlighttext>(.*?)</highlighttext>", r"\1", text)


def print_vacancies(vacancies: List[Vacancy]) -> None:
    """Метод выводит список вакансий в консоль"""

    for v in vacancies:
        name_clean = clean_highlight_tags(v.name)
        description_clean = clean_highlight_tags(v.description)
        print(
            f"Название: {name_clean}\nСсылка: {v.url}\nЗарплата: {v.salary}\nОписание: {description_clean}\n{"-" * 50}"
        )
