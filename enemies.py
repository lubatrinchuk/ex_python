# coding: utf-8
# license: GPLv3
import random
from gameunit import *
#задания питон 1 семестр

class Enemy(Attacker):
    pass

def generate_random_enemy():#рандомно выбираем врага
    RandomEnemyType = random.choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy


def generate_enemies_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list


class Dragon(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer


class GreenDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'зелёный'

    def question(self):
        x = random.randint(1,100)
        y = random.randint(1,100)
        self.__quest = str(x) + '+' + str(y) #создаем вопрос
        self.set_answer(x + y) #правильный ответ
        return self.__quest #задаем вопрос

class RedDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'красный'

    def question(self):
        x = random.randint(1,100)
        y = random.randint(1,100)
        self.__quest = str(x) + '-' + str(y) #создаем вопрос
        self.set_answer(x - y) #правильный ответ
        return self.__quest #задаем вопрос

class BlackDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'чёрный'

    def question(self):
        x = random.randint(1,100)
        y = random.randint(1,100)
        self.__quest = str(x) + '*' + str(y) #создаем вопрос
        self.set_answer(x * y) #правильный ответ
        return self.__quest #задаем вопрос

class Troll(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer

class WhiteTroll(Troll):
    def __init__(self):
        self._health = 200
        self._attack = 50
        self._color = 'белый'

    def question(self):
        x = random.randint(1,6)
        self.__quest = "угадай число от 1 до 5" #создаем вопрос
        self.set_answer(x) #правильный ответ
        return self.__quest #задаем вопрос

class GrayTroll(Troll):
    def __init__(self):
        self._health = 200
        self._attack = 50
        self._color = 'серый'

    def question(self):
        x = random.randint(1,100)
        self.__quest = str(x) + " - простое число? Напишите 1, если да, 0, если нет" #создаем вопрос
        numbers = [2, 3, 5,	7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        k = 0
        for i in range(len(numbers)):
            if x == numbers[i]:
                k += 1
        if k > 0:
            self.set_answer("да")  # правильный ответ
        else:
            self.set_answer("нет")  # правильный ответ
        return self.__quest #задаем вопрос

class BrownTroll(Troll):
    def __init__(self):
        self._health = 200
        self._attack = 50
        self._color = 'коричневый'

    def question(self):
        x = random.randint(1,100)
        self.__quest = "разложи " + str(x) + " на множители и перечисли их через запятую" # создаем вопрос
        div = []
        i = 1
        while x > 1:
            if x % i == 0:
                div.append(i)
                x = x // i
            i += 1
        self.set_answer(', '.join(map(str,div)))  # правильный ответ
        return self.__quest  # задаем вопрос

enemy_types = [GreenDragon, RedDragon, BlackDragon, WhiteTroll, GrayTroll, BrownTroll]
enemies_trolls = [WhiteTroll, GrayTroll, BrownTroll]
enemies_dragons = [GreenDragon, RedDragon, BlackDragon]