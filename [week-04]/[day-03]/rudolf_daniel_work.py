from random import randint

class Apple(object):
    def get_apple(self):
        return "apple"

class Sum(object):
    def summa(self, numbers):
        summarum = 0
        for i in numbers:
            summarum += i
        return summarum

class Anagram(object):
    def is_anagram(self, a, b):
        first_string = sorted(a)
        second_string = sorted(b)
        if first_string == second_string:
            return True
        else:
            return False

class CountLetters(object):
    def dictionary_maker(self, text):
        counter = {}
        for i in text:
            if i not in counter: 
                counter[i] = 1
            else:
                counter[i] += 1

        return counter

class Fibonacci(object):
    def fibonacci(self, number):
        if number < 2:
            return number
        else:
            return (self.fibonacci(number-1) + self.fibonacci(number-2))

class Sharpie(object):
    def __init__(self, color="", width=0.0):
        self.ink_amount = 100.0
        self.color = color
        self.width = width
    
    def use():
        self.ink_amount -=1

class Animal(object):
    def __init__(self):
        self.hunger = 50
        self.thirst = 50

    def eat():
        self.hunger -= 1
    
    def drink():
        self.thirst -= 1

    def play():
        self.hunger += 1
        self.thirst += 1

class CowsAndBulls(object):
    def __init__(self):
        number = randint(1000, 9999)
        game_state = playing
        counter = 0
        random_number_list = []
        new_number_list = []
        for i in number:
            random_number_list.append(i)
    
    def guess_result(self, guess):
        counter += 1
# Here comes the rest of the class.