# используется для сортировки

from operator import itemgetter


class Student:

    """Студент"""

    def __init__(self, id, fio, average_mark, group_id):

        self.id = id

        self.fio = fio

        self.average_mark = average_mark

        self.group_id = group_id


class Group:

    """Группа"""

    def __init__(self, id, number):

        self.id = id

        self.number = number


# Группы

groups = [

    Group(1, 'СМ10-61Б'),

    Group(2, 'ИУ7-61Б'),

    Group(3, 'ИУ6-23Б'),


    Group(11, 'ИУ3-45Б'),

    Group(22, 'МТ4-81Б'),

    Group(33, 'РК6-42Б'),

]


# Студенты

students = [

    Student(1, 'Артамонов', 3.5, 1),

    Student(2, 'Петров', 5.0, 2),

    Student(3, 'Иваненко', 4.5, 3),

    Student(4, 'Иванов', 4, 3),

    Student(5, 'Иванин', 3.7, 3),

]


def main():

    """Основная функция"""


    # Соединение данных один-ко-многим 

    one_to_many = [(s.fio, s.average_mark, g.number) 

        for g in groups 

        for s in students 

        if s.group_id==g.id]

    

    print('Задание 1')

    res_11 = sorted(one_to_many, key=itemgetter(2))

    print(res_11)

    

    print('\nЗадание 2')

    res_12_unsorted = []

    # Перебираем все группы

    for g in groups:

        # Список студентов группы

        g_students = list(filter(lambda i: i[2]==g.number, one_to_many))

        # Если в группе есть студенты        

        if len(g_students) > 0:

            # Средние баллы студентов

            g_average_marks = [average_mark for _,average_mark,_ in g_students]

            # Средний балл студентов в группе

            g_average_marks_avg = sum(g_average_marks) / len(g_average_marks)

            res_12_unsorted.append((g.number, g_average_marks_avg))


    # Сортировка по среднему баллу в группе

    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)

    print(res_12)


if __name__ == '__main__':

    main()

