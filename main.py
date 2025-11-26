import logging


from src.api import HeadHunterAPI
from src.vacancy import Vacancy
from src.utils import filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies, print_vacancies
from src.storage import JSONSaver

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

def user_interaction():
    """Метод, который взаимодействует с пользователем через информационный интерфейс"""

    logging.info("Старт приложения")
    hh_api = HeadHunterAPI()
    saver = JSONSaver()

    while True:
        print("\n1. Поиск и добавление вакансий\n2. Вывести топ N по зарплате\n3. Фильтрация по ключу"
              "\n4. Удалить вакансию\n0. Выйти\n")
        cmd = input("Выберите действие: ").strip()

        if cmd == "1":
            search_query = input("Введите поисковый запрос: ")
            hh_vacancies = hh_api.get_vacancies(search_query)
            vac_objs = Vacancy.cast_to_object_list(hh_vacancies)
            for vac in vac_objs:
                saver.add_vacancy(vac)
            print(f"Добавлено {len(vac_objs)} новых вакансий.")

        elif cmd == "2":
            n = int(input("Введите количество топовых вакансий: "))
            all_vacancies = saver.get_vacancies()
            sorted_vacancies = sort_vacancies(all_vacancies)
            top_vacancies = get_top_vacancies(sorted_vacancies, n)
            print_vacancies(top_vacancies)

        elif cmd == "3":
            keywords = input("Введите ключевые слова через пробел: ").split()
            all_vacancies = saver.get_vacancies()
            filtered = filter_vacancies(all_vacancies, keywords)
            print_vacancies(filtered)

        elif cmd == "4":
            url = input("Введите url вакансии для удаления: ").strip()
            all_vacancies = saver.get_vacancies()
            found = [v for v in all_vacancies if v.url == url]
            if found:
                saver.delete_vacancy(found[0])
                print("Вакансия удалена.")
            else:
                print("Вакансия не найдена.")

        elif cmd == "0":
            print("Выход.")
            break

        else:
            print("Некорректный ввод.")

if __name__ == "__main__":
    user_interaction()