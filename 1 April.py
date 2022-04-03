'''
#Q1). Write a program to reverse an integer in Python
num = input("Enter your number: ")
print(num[::-1])


#Q2). Write a program in Python to check whether an integer is Armstrong number or not.

def isArmstrong(num):
    sum=0
    for i in str(num):
        sum += int(i) ** 3

    if sum == int(num):
        return "Number is armstrong"
    else:
        return "number is not armstrong"

print(isArmstrong(101))
print(isArmstrong(1))


#Q3). Write a program in Python to check given number is prime or not.

def isPrime(num):
    if num<2:
        return "not prime"
    elif num == 2:
        return  "prime"
    else:
        for i in range(2,num):
            if num % i == 0:
               return "not prime"
        else:
            return "prime"
print(isPrime(7))


#Q4). Write a program in Python to print the Fibonacci series using iterative method.

num = int(input("Enter number: "))
a = 0
b = 1

for i in range (num):
    c= a+b
    print(a)
    a=b
    b=c


#Q5). Write a program in Python to print the fibonacci series using recursive method.

def fib (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib (n-2)

print(fib(10))



#Q6). Write a program in Python to check whether a number is palindrome or not using iterative method.
def pali(word):
    list_1 = [i.lower() for i in word]
    list_2 = [j.lower() for  j in word[::-1]]

    for a in range (len(list_1)):
        if list_1[a] != list_2[a]:
            return False
        else:
            return True
print(pali("mama"))
print(pali("Tenet"))

def pali (word):
    word = str(word)
    for i in range(len(word)):
        if word[i] != word[-i-1]:
            return False
        else:
            return True
print(pali(111))
print(pali(12321))


#Q8). Write a program in Python to find greatest among three integers.
a = [12,15,16]

print(max(a))

#Q9). Write a program in Python to check if a number is binary?

def isBin(num):
    for i in str(num):
        if i not in ['0', '1']:
            return False
        else:
            return True

print(isBin(1000))



#Q10). Write a program in Python to find sum of digits of a number using recursion?

def sum_digit(n):
    if len(str(n))==1:
        return n
    else:
        return int(str(n)[0])+sum_digit(int(str(n)[1:]))
print(sum_digit(125))



#Q11). Write a program in Python to swap two numbers without using third variable?

a=10
b=11

a,b = b,a

print(a)
print(b)


#Q12). Write a program in Python to swap two numbers using third variable?

a=10
b=11
tem=1

tem = a
a = b
b = tem

print(a)
print(b)


#Q13). Write a program in Python to find prime factors of a given integer.

def prime_fac (n):
    l = []
    i=2
    while n>1:
      if n % i ==0:
        l.append(i)
        n=n//i
      else:
          i+=1
    return l

print(prime_fac(15))



#Q14). Write a program in Python to add two integer without using arithmetic operator?

def ad_n (a,b):
    return  sum([a,b])

print(ad_n(12,13))

c=1
d=2
print(c.__add__(d))


#Q15). Write a program in Python to find given number is perfect or not?

def is_perfect(n):
    l=[]
    for i in range (1,n):
        if n%i == 0:
            l.append(i)
    if sum(l) == n:
        return True
    else:
        return False

print(is_perfect(6))
print(is_perfect(28))
print(is_perfect(496))



#Q16). Python Program to find the Average of numbers with explanations.

def average_num(*a):

    print(sum(a)/len(a))

average_num(12,13,14)


#Q17). Python Program to calculate factorial using iterative method.

def fact(num):
    mul = 1
    for i in range (1,num+1):
        mul *= i
    print(mul)
fact(5)


#Q18). Python Program to calculate factorial using recursion.

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))



#Q19). Python Program to check a given number is even or odd.

def is_even_odd (n):
    if n % 2 == 0:
        return  "Even"
    else :
        return "odd"

print(is_even_odd(15))



#Q20). Python program to print first n Prime Number with explanation.



def is_prime(n):
    if n == 2:
        return True
    else:
        for i in range (2,n):
            if n%i == 0:
                return  False
        else:
            return True

#r = int(input("Enter stop number: "))
c=0
r=10
for i in range (2,1000):
    if is_prime(i) ==  True and c<r:
        print(i)
        c+=1
    else:
        continue


#Q21). Python Program to print Prime Number in a given range
num= 10

for n in range(2,num):
    for i in range(2,n):
        if(n%i==0):
                 break
    else:
        print(n)


#Q22). Python Program to find Smallest number among three.

def smallest_num(*a):
    print(min(a))

smallest_num(14,10,16)


#Q23). Python program to calculate the power using the POW method.

a= 2
b=8
print(a.__pow__(b))

print(pow(a,b))



#Q24). Python Program to calculate the power without using POW function.(using for loop)

a = int(input("Enter Number: "))
b= int(input("Enter power: "))
mul = 1
for i in range(b):
     mul*=a
print(mul)



#Q25). Python Program to calculate the power without using POW function.(using while loop).
a = int(input("Enter Number: "))
b= int(input("Enter power: "))
mul = 1
c=0

while c<b:
    mul *= a
    c+=1
print(mul)

'''

base = 3
exponent = 4

result = 1

while exponent != 0:
    result *= base
    exponent-=1

print("Answer = " + str(result))







