
#Exercise 1: Print First 10 natural numbers using while loop
i=1
while i <11:
    print(i)
    i+=1

#Exercise 2: Print the following pattern
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5

for i in range(1,6):
    for j in range(1,i+1):
        print (j, end=' ')
    print()


#Exercise 3: Calculate the sum of all numbers from 1 to a given number
a = int(input("Enter Number: "))
s=0
for i in range (1,a+1):
    s+=i
print (s)

#Exercise 4: Write a program to print multiplication table of a given number
a = int(input("Enter Number: "))
mul=1
for i in range(1,11):
    print (a, "*", i ,'=',a*i)


#Exercise 5: Display numbers from a list using loop
#Write a program to display only those numbers from a list that satisfy the following conditions
#The number must be divisible by five
#If the number is greater than 150, then skip it and move to the next number
#If the number is greater than 500, then stop the loop
#numbers = [12, 75, 150, 180, 145, 525, 50]

numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:
    if i>500:
        break
    else:
        if i%5==0:
            if i>150:
                continue
            else:
                print(i)

for i in numbers:
    if i>500:
        break
    elif i>150:
        continue
    elif i%5==0:
        print(i)


# Exercise 6: Count the total number of digits in a number

a= input("Enter number: ")
c=0
for i in a:
    c+=1
print (c)


#Exercise 7: Print the following pattern
#5 4 3 2 1
#4 3 2 1
#3 2 1
#2 1
#1

for i in range (5,0,-1):
    for j in range (i,0,-1):
        print (j, end=' ')
    print()


#Exercise 8: Print list in reverse order using a loop
#Given: list1 = [10, 20, 30, 40, 50]

list1 = [10, 20, 30, 40, 50]

for i in range(len(list1)-1,-1,-1):
    print(list1[i])

#Exercise 9: Display numbers from -10 to -1 using for loop
for i in range (-10,0):
    print(i)


#Exercise 10: Use else block to display a message “Done” after successful execution of for loop

for i in range(1,5):
    print(i)
else:
    print('Done')


#Exercise 12: Display Fibonacci series up to 10 terms

a=0
b=1


for i in range(1,11):
    s=a+b
    print (a, end=' ')
    a=b
    b=s


#Exercise 13: Find the factorial of a given number

a = int(input("Enter Number: "))

mul=1
for i in range (1,a+1):
    mul*=i
print (mul)


#Exercise 14: Reverse a given integer number
a= input("Enter Number ")

s=''
for i in range(len(a)-1,-1,-1):
    s= s+a[i]
print(s)

#Exercise 15: Use a loop to display elements from a given list present at odd index positions
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in range (1,len(my_list),2):
    print(my_list[i], end=' ')

#Exercise 16: Calculate the cube of all numbers from 1 to a given number
a = int(input("Enter Number: "))

for i in range (1, a+1):
    print ("Number is {}. Its Cube is {}".format(i, i**3))


#Exercise 17: Find the sum of the series upto n terms
#Write a program to calculate the sum of series up to n term. For example, if n =5
# the series will become 2 + 22 + 222 + 2222 + 22222 = 24690

a=2
s=0
n=5
for i in range (1,n+1):
    s= s+ int(str(a)*i)
print(s)


#Exercise 18: Print the following pattern
#*
#* *
#* * *
#* * * *
#* * * * *
#* * * *
#* * *
#* *
#*

for i in range (1,6):
    print (i*'* ')
for i in range (4,0,-1):
    print (i*'* ')





