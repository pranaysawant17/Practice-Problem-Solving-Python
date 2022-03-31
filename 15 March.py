'''
# Multiplication Table
def mul_tab(a):
    for i in range(1,11):
        print( '{} * {} = {}'.format(a,i,a*i) )

num = int(input(" Enter Your Number: "))
mul_tab(num)


# Write a program to print twin prime number less than 1000.
def prime (a):

    if a < 3:
        return False
    else:
        for i in range (2,a):
            if a%i == 0:
                return False
        else:
            return True
for i in range(1000):
    if prime(i) == True and prime (i+2) == True:
        print(i,i+2)

def isPrime(a) :
    count = 0
    for i in range(1, a+1) :
        if a % i == 0 :
            count = count + 1
    if count == 2:
            return True
n = 2
N = int(input("Enter the value of N : "))
while n < N :
    if isPrime(n) == True and isPrime(n+2) == True:
        print("({0},{1})".format(n, n+2), end = "    ")
    n = n + 1



#Write program for prime factor of number

def prime_factor (a):
    for i in range (2,a):
        while a%i == 0:
            print (i, end=' ')
            a=a//i
    else:
        if a>1:
            print(a)

prime_factor(56)



# Write a program to perform permutation and combination
def fact(a):
    mul = 1
    for i in range (1,a+1):
        mul*=i
    return mul

def permutation (n,r):
    return fact(n)/ fact(n-r)
def combination (n,r):
    return fact(n)/(fact(r)*fact(n-r))

print(permutation(5,3))
print(combination(5,3))

#write a function that converts a number from decimal to binary
def bin(a):
    s=''
    while a>0:
        s += str(a % 2)
        a=a//2
    return s[::-1]

print(bin(10))


#write a function cubesum() which returns sum of cube of individual digit of that integer. Also write function isArmstrong()
# PrintArmstrong() to identify and print Armastrong number.

def cubesum(a):
    sum= 0
    for i in str(a):
        sum+= int(i)**3
    return sum

def isArmstrong(a):
    if cubesum(a)==a:
        return True
    else:
        return False

def PrintArmstrong(n):
    for i in range (2,n+1):
        if isArmstrong(i) == True:
            print(i)

print(cubesum(128))
print(isArmstrong(370))
PrintArmstrong(1000)


#Write a function prodDigits() that returns product of digits of given number

def prodDigits(n):
    mul=1
    for i in str(n):
        mul*= int(i)
    return  mul
print(prodDigits(21))

# Using prodDigits() write a program for MDR () and Mpersistence().
def MDR (a):
    while a>9:
          a=prodDigits(a)
    else:
        return (a)

def Mpersistence(a):
    c=0
    while a>9:
          a=prodDigits(a)
          c+=1
    else:
        return c

print(Mpersistence(86))
print(MDR(86))


#9. Write a function sumPdivisors() that finds the sum of proper divisors of a number. Proper  divisors of a number
# are those numbers by which the number is divisible, except the  number itself.
#For example proper divisors of 36 are 1, 2, 3, 4, 6, 9, 18

def sumPdivisors (a):
    lst=[]
    sum = 0
    for i in range(1,a):
        if a%i == 0:
            sum += i
            lst.append(i)
    return  sum

print(sumPdivisors(36))

#10. A number is called perfect if the sum of proper divisors of that number is equal to the  number. For example 28
# is perfect number, since 1+2+4+7+14=28. Write a program to  print all the perfect numbers in a given range
def perfectNumber (a):
    for i in range (1,a+1):
        if sumPdivisors(i)== i:
            print(i)
perfectNumber(1000)


# Two different numbers are called amicable numbers if the sum of the proper divisors of  each is equal to the other number.
# For example 220 and 284 are amicable numbers.
#Sum of proper divisors of 220 = 1+2+4+5+10+11+20+22+44+55+110 = 284
#Sum of proper divisors of 284 = 1+2+4+71+142 = 220
#Write a function to print pairs of amicable numbers in a range

def amicableNum (a):
    for i in range(1,a+1):
        for j in range (1, a+1):
            if sumPdivisors(i)  == j and sumPdivisors(j) == i and i!=j:
                print (i,j)

amicableNum(1000)


#12. Write a program which can filter odd numbers in a list by using filter function

a = [ 1,6,8,9,45,64.5,22]

print(list(filter(lambda x: x%2==0, a)))

#13. Write a program which can map() to make a list whose elements are cube of elements in  a given list
a = [1,2,3,8,9,11]
print(list(map(lambda x: x**3, a)))


#14. Write a program which can map() and filter() to make a list whose elements are cube of  even number in a given list.
a = [ 1,6,8,9,45,64,5,22]
print(list(map(lambda x:x**3,list(filter(lambda x:x%2==0,a)))))

'''

class Comp:

    def config(self):
        print("Aprajita")

c=Comp()

Comp.config(self=c)
c.config()