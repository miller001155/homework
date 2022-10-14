'''Задача 72'''
school_subjects = ['mathematic', 'physics', 'literature', 'physical_education', 'social_studies',
                   'labour']  # список школьных предметов
user_unloved_items = (input('какие предметы вам не нравятся:')).split()  # спрашиваем какие предметы не нравятся
for items in user_unloved_items:  # создаем цикл в котором перебираем те предметы которые ввел пользователь
    if items in school_subjects:  # проверяем есть ли предмет в списке
        school_subjects.remove(items)  # удаляем из списка
print(school_subjects)  # выводим новый список на экран
