'''
#1 Table of input number
def table_num(a):
    for i in range (1,11):
        print (a, "*", i, "=", a * i)

n= int(input("Enter your number:"))
(table_num(n))

#2 Twin Prime Number

def is_Prime (a):
    if a > 1:
        for i in range (2,a):
            if a%i == 0:
                return False

        else:
            return True
    else:
        return False

n = int(input("Enter Your Number"))
for j in range (n):
    if (is_Prime(j)== True) and (is_Prime(j+2)==True):
        print ((j , j+2 ), end=" ")
    else:
        pass

print(is_Prime(10))
print(is_Prime(7))
print(is_Prime(37))



def is_Prime(z):

    return all(z%y!=0 for y in range(2,z))


print([(i, i+2) for i in range(2,100) if is_Prime(i)== True and is_Prime(i+2)==True])

def prime_fac(a):
    for i in range(2, a):
        while a % i == 0:
            print(i, end=" ")
            a = a // i
    else:
        if a>1:
         print(a)

#a = int(input("Enter your number="))
prime_fac (13)

def factorial(num):

  #This function provides the factorial of given number

  mult=1
  for i in range (1, num+1):
    mult*=i
  return mult

n= int(input("Enter number of Objects: "))
r= int (input("Enter number of times object taken: "))

permutation = factorial(n)/factorial(n-r)
combination = factorial (n)/(factorial(r)*factorial(n-r))

print ("Permutation is:", permutation ,'\n' ,"Combination is: ", combination)



def binary(a):

  #This function provides binary number of given number.


  bin=[]
  while a>0:
    c=int(a%2)
    bin.append(c)
    a=(a-c)/2
  #bin.append(0)

  b = ''
  for i in reversed(bin):
    b += str(i)
  print ("Binary number =",b)

binary(12)
print(bin(12))

def cubesum(a):

  #This function gives sum of cube of the digits of number.

  list=[int(i) for i in str(a)]
  b=0
  for i in list:
   c=i ** len(list)
   b= b+c
  return(b)

#n= int(input('Enter your number:'))
#print(cubesum(n))


def isArmstrong(d):
    
    #This function checks if given number is Armstrong or not.
    
    if cubesum(d) == d:
        return True
    else:
        return False


def printArmstrong(e):
    
    #This function prints Armstrong numbers in given range
    
    for i in range(e):
        if isArmstrong(i) == True:
            print("Armstrong number = ", i)
        else:
            continue


rangeNum = int(input("Enter last number of range: "))

printArmstrong(rangeNum)


def prodDigits(a):

  list=[int(i) for i in str(a)]
  b=1
  for i in list:
    b=b*i
  return b
#print(prodDigits(2489))

def MDR(e):
   
   

    while prodDigits(e) > 10:
        e = prodDigits(e)
        print(e)

    else:
        print("MDR is: ", prodDigits(e))


def MPersistence(e):
   
    counter = 0
    while prodDigits(e) > 10:
        e = prodDigits(e)
        counter += 1
    else:
        counter += 1
        print("Mpersistence is: ", counter)

(MPersistence(234))
(MDR(124))'''

def sumPdivisors(a):
  '''
  This function gives sum of proper divisors of given numbers.
  '''
  sum = 0
  for i in range (1, a):
    if a%i == 0:
      sum+=i

    else:
      continue

  return sum



sumPdivisors(56)




def amicableNumber(a):
  '''
  This function gives amicable numbers.
  '''
  for i in range (a):
     for  j in range (a):
        if (sumPdivisors (i)== j and sumPdivisors (j) == i) and (i != j):
            print("Sum",i, "is",sumPdivisors (i))
            print("sum" ,j, "is",sumPdivisors(j))

            print (i,j)
        else:
          continue
amicableNumber(1000)