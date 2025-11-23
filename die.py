from random import randint


class Die:
    """класс представляющий кубик"""

    def __init__(self, num_sides=6):
        """по умолчанию используем один кубик"""
        self.num_sides = num_sides

    def roll(self):
        """возвращает случайное число от 1 до num_sides"""
        return randint(1, self.num_sides)
