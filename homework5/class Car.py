class Car:
    def __init__(self, stamp, model, year):
        self.stamp = stamp
        self.model = model
        self.year = year
        self.speed = 0

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


opel = Car('opel', 'Astra', 2010,)