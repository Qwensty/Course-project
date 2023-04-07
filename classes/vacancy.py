class Vacancy:
    __slots__ = ('name', 'url', 'description', 'salary', 'date_published')

    def __init__(self, data: dict):

        self.name = data['name']
        self.url = data['url']
        self.description = data['description']
        self.salary = data.get('salary')
        self.date_published = data['date_published']

    def __gt__(self, other) -> bool:
        return self.date_published > other.date_published

    def __lt__(self, other) -> bool:
        return self.date_published < other.date_published

    def __str__(self) -> str:
        return f'Вакансия - {self.name}, заработная плата - {self.get_salary()}'

    def get_salary(self) -> str:
        """Возвращает зарплату в отформативанном виде"""

        if self.salary is not None:

            if self.salary.get('from') not in [0, None] and self.salary.get('to') not in [0, None]:
                return f"от {self.salary.get('from')} до {self.salary.get('to')} руб/мес"

            elif self.salary.get('from') == 0 or None and self.salary('to') == 0 or None:
                return 'не указана'

            elif self.salary.get('from') in [0, None] and self.salary.get('to') not in [0, None]:
                return f"до {self.salary.get('to')} руб/мес"

            elif self.salary.get('from') not in [0, None] and self.salary.get('to') in [0, None]:
                return f"от {self.salary.get('from')} руб/мес"

        return 'не указана'

class HHVacancy(Vacancy):
    """ HeadHunter Vacancy """

    def __str__(self) -> str:
        return f'HH: {self.name}, зарплата: {self.get_salary()}'


class SJVacancy(Vacancy):
    """ SuperJob Vacancy """

    def __str__(self) -> str:
        return f'SJ: {self.name}, зарплата: {self.get_salary()}'

