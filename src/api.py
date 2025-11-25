from abc import ABC, abstractmethod


import requests
import logging
from typing import List

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')


class AbstractApi(ABC):
    """Абстрактный класс для API"""

    @abstractmethod
    def _connect(self) -> requests.Response:
        """Метод осуществляет подключение к API"""
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str) -> List[dict]:
        """Метод получает список вакансий по ключевому слову"""
        pass


class HeadHunterAPI(AbstractApi):
    """Класс для работы с API hh.ru"""

    __BASE_URL = "https//api.hh.ru/vacancies"

    def _connect(self) -> requests.Response:
        """ Метод подключается к hh.ru и проверяет статус"""

        logging.info("Подключение к API hh.ru...")
        response = requests.get(self.__BASE_URL)
        if response.status_code != 200:
            logging.error(f"Ошибка подключения: {response.status_code}")
        logging.info("Успешное подключение к API hh.ru")
        return response

    def get_vacancies(self, keyword: str, per_page: int = 100) -> List[dict]:
        """Метод получает вакансии по ключу"""

        self._connect()
        params = {
            "text": keyword,
            "per_page": per_page,
            "page": 0,
            "area": 113,
            "only_with_salary": False
        }
        logging.info(f"Запрашиваем вакансии по ключу: '{keyword}'")
        response = requests.get(self.__BASE_URL, params=params)
        if response.status_code != 200:
            logging.error(f"Ошибка получения вакансий: {response.status_code}")
            raise ConnectionError(f"Ошибка получения вакансий: {response.status_code}")
        results = response.json().get("items", [])
        logging.info(f"Получено {len(results)} вакансий")
        return results
