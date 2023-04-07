import os

from classes.engine import Engine, HH, SuperJob
from utils.utils import get_top_vacancies_by_date, print_info, check_search, \
    get_top_vacancies_by_to_salary


def main() -> None:

    path = os.path.join('data/all.json')
    connector = Engine.get_connector(path)

    # поиск вакансии по запросу
    while True:

        search = input("Введите слово, по которому будем искать вакансию\n")

        while True:
            search_experience = input("Будем искать вакансии без опыта работы? Y/N\n")
            if search_experience.upper() not in ['Y', 'N']:
                print('Введите Y или N')
                continue
            else:
                break

        if search_experience.upper() == 'Y':
            hh = HH(search, 'noExperience')
            sj = SuperJob(search, 'noExperience')

        else:
            hh = HH(search)
            sj = SuperJob(search)

        if check_search(hh, sj):
            all_vacancies = hh.get_vacancies() + sj.get_vacancies()
            connector.insert(all_vacancies)
            break
        else:
            print('Такой вакансии нет')
            continue

    # запрос количества вакансий для вывода
    while True:
        top_count = input('Укажите какое количество вакансий будем выводить на экран\n')
        if not top_count.isdigit() or int(top_count) <= 0:
            print('Количество должно быть целым числом больше ноля. Попробуйте еще раз')
            continue
        else:
            top_count = str(int(top_count))
            break

    vacancies = connector.select({})

    # меню
    while True:
        print(f'Меню:\n\
                        1 - вывести {top_count} последних вакансии\n\
                        2 - вывести топ-{top_count} вакансий заработку\n\
                        stop - закончить работу')
        print()
        user_input = input("Введите нужный вариант\n")

        if user_input == '1':
            data = get_top_vacancies_by_date(data=vacancies, top_count=top_count)
            print_info(data)

        elif user_input == '2':
            data = get_top_vacancies_by_to_salary(data=vacancies, top_count=top_count)
            print_info(data)

        elif user_input.lower() == 'stop':
            print('Программа завершает работу')
            break

        else:
            print("Такого варианта нет, попробуйте еще раз")
            continue

        print('Показать еще меню? Y/N')
        choice = input().upper()
        if choice == 'Y':
            continue
        else:
            print('Программа завершает работу')
            break

    exit()


if __name__ == '__main__':
    main()
