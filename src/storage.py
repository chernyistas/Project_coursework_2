import json
import logging
import os
from typing import List, Optional, Any
from src.vacancy import Vacancy
from abc import ABC, abstractmethod

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

class AbstractFileHandler(ABC):
    """Абстрактный класс-хранилище вакансий"""

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy):
        """Добавляет вакансию"""
        pass

    @abstractmethod
    def get_vacancies(self, criteria: Optional[Any] = None) -> List[Vacancy]:
        """Получает вакансии с опциональным фильтром"""
        pass


    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy):
        """ Удаляет вакансию"""
        pass


class JSONSaver(AbstractFileHandler):
    """Клас для работы с JSON-файлом вакансий"""

    def __init__(self, filename: str = "data/vacancies.json"):
        """Конструктор инициализирующий JSONSaver"""
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        self.__filename = filename

    def add_vacancy(self, vacancy: Vacancy):
        """Добавляет вакансию"""
        logging.info(f"Пробуем добавить вакансию: {vacancy.name}")
        vacancies = self.get_vacancies()
        if not any(v.url == vacancy.url for v in vacancies):
            vacancies.append(vacancy)
            self.__save_to_file(vacancies)
            logging.info(f"Вакансия {vacancy.name} добавлена")
        else:
            logging.info(f"Вакансия уже есть: {vacancy.url}")

    def get_vacancies(self, criteria: Optional[Any] = None) -> List[Vacancy]:
        """Получает вакансии с опциональным фильтром"""
        try:
            with open(self.__filename, "r", encoding="utf-8") as f:
                data = json.load(f)
            vacancies = [Vacancy(d["name"], d["url"], d["salary"], d["description"]) for d in data]
        except Exception as e:
            logging.error(f" Ошибка чтения файла: {e}")
            vacancies = []
        if criteria:
            return [v for v in vacancies if criteria(v)]
        return vacancies

    def delete_vacancy(self, vacancy: Vacancy):
        """ Удаляет вакансию"""
        logging.info(f"Удаляем вакансию: {vacancy.name}")
        vacancies = self.get_vacancies()
        vacancies = [v for v in vacancies if v.url != vacancy.url]
        self.__save_to_file(vacancies)

    def __save_to_file(self, vacancies: List[Vacancy]):
        try:
            data = [{"name": v.name, "url": v.url, "salary": v.salary, "description": v.description} for v in vacancies]
            with open(self.__filename, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            logging.info(f"Вакансии успешно сохранены в {self.__filename}")
        except Exception as e:
            logging.error(f"Ошибка при сохранении в файл: {e}")

