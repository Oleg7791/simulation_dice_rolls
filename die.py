import random


class Die:
    """ класс представляющий один кубик"""

    def __init__(self, num_sides=6):
        """по умолчанию используется шестигранный кубик"""
        self.num_sides = num_sides

    def roll(self):
        """возвращает случайное число от1 до num_sides"""
        return random.randint(1, self.num_sides)
