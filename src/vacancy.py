from typing import Optional, List
import re

class Vacancy:
    """ Класс, представляющий вакансию"""

    __slots__ = ["name", "url", "salary", "description"]

    def __init__(self, name: str, url: str, salary: Optional[str], description: str):
        """Конструктор, инициализирующий вакансию"""
        self.name = name
        self.url = url
        self.salary = self._validate_salary(salary)
        self.description = description

    def _validate_salary(self, salary: Optional[str]) -> str:
        """Метод, валидирующий значение зарплаты"""

        return salary if salary else "Зарплата не указана"

    def __lt__(self, other: "Vacancy") -> bool:
        """Метод проверяющий, что зарплата меньше определённой зарплаты"""
        return self._salary_value(self.salary) < self._salary_value(other.salary)

    def __gt__(self, other: "Vacancy") -> bool:
        """Метод проверяющий, что зарплата больше определённой зарплаты"""
        return self._salary_value(self.salary) > self._salary_value(other.salary)

    def __eq__(self, other: "Vacancy") -> bool:
        """Метод проверяющий, что зарплата равна определённой зарплате"""

    @staticmethod
    def _salary_value(salary: str) -> int:
        """Метод, получающий числовое значение зарплаты для сравнения"""

        if salary == "Зарплата не указана":
            return 0
        match = re.search(r'\d+', salary.replace(' ', ''))
        return int(match.group()) if match else 0

    @classmethod
    def cast_to_object_list(cls, vacancies_jason: List[dict]) -> List["Vacancy"]:
        """Метод, конвертирующий список словарей API в список словарей JSON"""

        list_vac = []
        for item in list_vac:
            name = item.get("name", "Без названия")
            url = item.get("alternate_url", "")
            salary_data = item.get("salary")
            salary_str = None
            if salary_data:
                sf, st, cur = salary_data.get("from"), salary_data.get("to"), salary_data.get("currency", "")
                if sf and st:
                    salary_str = f"{sf} - {st} {cur}"
                elif sf:
                    salary_str = f"от {sf} {cur}"
                elif st:
                    salary_str = f"до {st} {cur}"
            description = item.get("snippet", {}).get("requirement", "")
            list_vac.append(cls(name, url, salary_str, description))
        return list_vac
