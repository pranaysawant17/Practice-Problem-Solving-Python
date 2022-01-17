'''
#Exercise 41. Rectangle class:

class Rectangle:
    def __init__(self, length , width):
        self.length = length
        self.width = width

    def perimeter(self):
        return self.length*2 + self.width*2
        #print('Per:' ,self.length*2 + self.width*2)

    def area (self):
        return self.length * self.width

    def display (self):
        print("Perimeter = ", self.perimeter())
        print("Area = ", self.area())

class Parallelepiped (Rectangle):
    def __init__(self, length, width , height):
        Rectangle.__init__(self, length , width)
        self.height = height
    def volume (self):
        return self.height * self.length * self.width
    def display(self):
        print("Volume ", self.volume())
class Square(Rectangle):
    def __init__(self, length , width , x):
        Rectangle.__init__(self, length, width)
        self.x = x
    def AreaSquare(self):
        print ("Area of squre =", self.x ** 2)



Rect1 = Rectangle (12, 30)
Rect1.display()
Pap1 = Parallelepiped (12,20,5)
Pap1.display()
Sq1= Square (10, 10 , 12)
Sq1.AreaSquare()

#Exercice 42: Person class and child Student class

class Person:
    def __init__(self, name , age):
        self.name = name
        self.age = age
    def display (self):
        print("Name of the person : " , self.name)
        print("Age of the person : ", self.age)
class Student(Person):
    def __init__(self, name, age , section):
        Person.__init__(self, name , age)
        self.section = section
    def displayStudent(self):
        print("Name of the Student : ", self.name)
        print("Age of the Student : ", self.age)
        print("Section of the Student : ", self.section)

Per1 = Person ("Ramesh Gir",37)
Per1.display()
Stud1= Student ("Rajiv Mishra", 13 , "10A")
Stud1.displayStudent()
'''
#Exercise 43. Bank Account class:

class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def deposit(self, dep):
        self.balance = self.balance + dep


    def Withdrawal (self, wit):
        if self.balance < wit:
            print("Not enough account balance")
        else:
            self.balance = self.balance - wit
    def bankFees(self):
        self.balance = (95/100) * self.balance
    def display (self):
        print( "Account Number: ", self.accountNumber)
        print("Name : ", self.name)
        print("Balance : " ,self.balance)

bank1 = BankAccount("A1245","Rakesh Kumar", 3000 )
bank1.deposit(200)
bank1.Withdrawal(400)
bank1.bankFees()
bank1.display()



