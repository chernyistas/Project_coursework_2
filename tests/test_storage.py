import os
import tempfile
from typing import List

from src.storage import JSONSaver
from src.vacancy import Vacancy


def test_json_saver_add_get_delete(vac_1: Vacancy) -> None:
    """Тест на корректность добавления, получения и удаления вакансий в JSON-файле"""

    with tempfile.NamedTemporaryFile(delete=False) as tf:
        filename: str = tf.name

    saver: JSONSaver = JSONSaver(filename)
    saver.add_vacancy(vac_1)
    all_vac: List[Vacancy] = saver.get_vacancies()
    assert any(v.url == "url" for v in all_vac)

    saver.delete_vacancy(vac_1)
    all_vac = saver.get_vacancies()
    assert all(v.url != "url" for v in all_vac)

    os.remove(filename)
