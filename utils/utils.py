from classes.engine import HH, SuperJob
from classes.vacancy import SJVacancy, HHVacancy


def print_info(data: list | str) -> None:
    """
    Вывод построчно с нумерацией, если список, либо вывод строки
    """
    if isinstance(data, list):
        count = 1
        for item in data:
            print(f'{count} - {item}')
            count += 1
    else:
        print(data)


def get_vacancies(vacancies: list) -> list[HHVacancy | SJVacancy]:
    """
    Возвращает экземпляры HHVacancy/SJVacancy
    """
    vacancies_list = []
    for vacancy in vacancies:
        if vacancy['source'] == "HeadHunter":
            vacancies_list.append(HHVacancy(vacancy))
        else:
            vacancies_list.append(SJVacancy(vacancy))
    return vacancies_list


def get_top_vacancies_by_to_salary(data: list, top_count: str) -> list:
    """
    Возвращает top_count вакансий по максимальной зарплате
    """

    # Перебор данных из файла по зарплате
    vacancies = []
    for item in data:
        if item.get('salary') is None or item.get('salary').get('from') is None:
            continue
        else:
            vacancies.append(item)

    # Сортировка по зарплате
    vacancies.sort(key=lambda k: k['salary']['from'], reverse=True)
    top_vacancies = vacancies[:top_count]

    if len(top_vacancies) == 0:
        return "В вакансиях не указана зарплата"
    else:
        return get_vacancies(top_vacancies)


def check_search(hh: HH, sj: SuperJob) -> bool:
    """
    Проверка на существование вакансии
    """
    return hh.get_request()['items'] != [] or sj.get_request()['objects'] != []


def get_top_vacancies_by_date(data: list, top_count: str) -> list:
    """
    Сортирует по дате
    """
    vacancies = get_vacancies(data)
    return sorted(vacancies, reverse=True)[:top_count]
