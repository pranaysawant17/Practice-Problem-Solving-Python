'''
#8. Write a Python class to reverse a string word by word. Go to the editor
#Input string : 'hello .py'
#Expected Output : '.py hello'

class Reverse:
    def __init__(self, a):
        self.a = a

    def rev_string(self):
        print(*self.a.split()[::-1])

ab=Reverse('hello .py')

ab.rev_string()

#9. Write a Python class which has two methods get_String and print_String. get_String
# accept a string from the user and print_String print the string in upper case.

class UpperStr:
    def get_string(self):
        self.a = input("Enter String: ")

    def print_String (self):
        print(self.a.upper())

ab = UpperStr()
ab.get_string()1
ab.print_String()
'''
from math import *
print(-log(0.5,2))
print(-0.4*log(0.4,2)-0.6*log(0.6,2))