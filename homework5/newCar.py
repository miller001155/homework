import class_Car  # импортируем модуль из предыдущего файла
my_mercedes = class_Car.Car('Mercedes', 'E500', 2000)  # создаем объект из класса Car
print(my_mercedes.get_descriptive_name())  # вывод информации на экран
my_mercedes.speed_limit()  # вводим новую функцию в предыдущем классе и используем ее
my_mercedes.speed_display()  # выводим скорость на экран!

