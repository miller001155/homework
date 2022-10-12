class Car:
    def __init__(self, stamp, model, year):
        self.stamp = stamp
        self.model = model
        self.year = year
        self.speed = 0
    def get_descriptive_name(self):
        '''Возвращает аккуратно отформотированное описание'''
        long_name = f'{self.year} {self.stamp} {self.model}'
        return long_name.title()

    def speed_up(self):
        self.speed += 5

    def speed_down(self):
        self.speed -= 5

    def stop(self):
        self.speed = 0

    def speed_display(self):
        print(self.speed)

    def reverse_gear(self):
        self.speed = - self.speed

    def speed_limit(self):
        self.speed = f'100 км/ч'


opel = Car('opel', 'Astra', 2010,)