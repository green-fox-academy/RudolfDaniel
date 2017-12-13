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