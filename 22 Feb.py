
# Question: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between
# 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

print(str([i for i in range(2000,3201) if (i%7 ==0) & (i%5 !=0)]).strip('[]'))


#Question: Write a program which can compute the factorial of a given numbers. The results should be printed in a
# comma-separated sequence on a single line. Suppose the following input is supplied to the program: 8 Then,
# the output should be: 40320
a = int(input(" Enter the number : "))

mul=1
for i in range(1,a+1):
    mul*=i
print (mul)


#Question: With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is
# an integral number between 1 and n (both included). and then the program should print the dictionary. Suppose the
# following input is supplied to the program: 8 Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

a= int(input("Enter number :"))

print({i : i**2 for i in range (1,a+1)})


#Question: Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a
# tuple which contains every number. Suppose the following input is supplied to the program: 34,67,55,33,12,98 Then, the
# output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')

a = input("Enter numbers seperated by comma: ")
lst=(a.split(','))
print(lst)
print(tuple(lst))


#Question: Write a program that calculates and prints the value according to the given formula: Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H: C is 50. H is 30. D is the variable whose values should be input to your
# program in a comma-separated sequence. Example Let us assume the following comma separated input sequence is given to
# the program: 100,150,180 The output of the program should be: 18,22,24

D = input(" Enter sequence of numbers: ")
C=50
H=30

lst=[]
for i in D.split(','):
    Q = round(((2*C* int(i))/H)**0.5)
    lst.append(Q)
print(str(lst).strip('[]'))

#Question: Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in
# the i-th row and j-th column of the array should be i*j. Note: i=0,1.., X-1; j=0,1, Y-1. Example Suppose the
# following inputs are given to the program: 3,5
# Then, the output of the program should be: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

a = input("Enter values :")
dim = a.split(',')

lst=[]
for i in range(int(dim[0])):
    lst1=[]
    for j in range(int(dim[1])):
        lst1.append(i*j)
    lst.append(lst1)
print(lst)


#Question: Write a program that accepts a comma separated sequence of words as input and prints the words in a
# comma-separated sequence after sorting them alphabetically. Suppose the following input is supplied to the program:
# without,hello,bag,world Then, the output should be: bag,hello,without,world

a = input(" Enter sequence of words ")
print(str(sorted(a.split(','))).strip('[]'))



#Question£º Write a program that accepts sequence of lines as input and prints the lines after making all characters in
# the sentence capitalized. Suppose the following input is supplied to the program: Hello world Practice makes perfect
# Then, the output should be: HELLO WORLD PRACTICE MAKES PERFECT

num = int(input("Enter number lines to input: "))

lst=[]
for i in range(num):
    a= input("Enter Line: ")
    lst.append(a.upper())
for j in lst:


#Question: Write a program that accepts a sequence of whitespace separated words as input and prints the words after
# removing all duplicate words and sorting them alphanumerically. Suppose the following input is supplied to the
# program: hello world and practice makes perfect and hello world again Then,
# the output should be: again and hello makes perfect practice world

a = input(" Enter sentence: ")
print (str(sorted(list(set(a.split(' '))))).strip('[]'))

lst=sorted(list(set(a.split(' '))))
print(*lst , sep=' ')


#Question: Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then
# check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma
# separated sequence. Example: 0100,0011,1010,1001 Then the output should be: 1010 Notes: Assume the data is input by console.

a = input("Enter list: ")
lst = a.split(',')
for i in lst:
    if  int(i,2) % 5 ==0:
        print(i)


#Question: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit
# of the number is an even number. The numbers obtained should be printed in a comma-separated sequence on a single line.
lst=[]
for i in range (1000,3001):
    a=str(i)
    if  (int(a[0])%2 ==0) & (int(a[1])%2 ==0) & (int(a[2])%2 ==0) & (int(a[3])%2 ==0)  :
        lst.append(i)
print(*lst, sep=',')


#Question: Write a program that accepts a sentence and calculate the number of letters and digits. Suppose the following
# input is supplied to the program: hello world! 123 Then, the output should be: LETTERS 10 DIGITS 3

a = input("Enter sen: ")
l=0
d=0
for i in a:
    if i.isdigit():
        d+=1
    elif i.isalpha():
        l+=1
    else:
        pass
print ('Letter',l, 'digits', d)



#Question: Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program: Hello world! Then, the output should be: UPPER CASE 1 LOWER CASE 9

a = input("Enter sen :")
u=0
l=0

for i in a:
    if i.isupper():
        u+=1
    elif i.islower():
        l+=1
    else:
        pass
print("Upper Case", u, "Lower Case", l)



#Question: Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a. Suppose the
# following input is supplied to the program: 9 Then, the output should be: 11106

a = input("Enter number")

a1=  a
a2 = a+a
a3 = a+a+a
a4 = a+a+a+a

print( int(a1)+int(a2)+ int(a3)+int(a4))



#Question: Use a list comprehension to square each odd number in a list. The list is input by a sequence of
# comma-separated numbers. Suppose the following input is supplied to the program: 1,2,3,4,5,6,7,8,9
# Then, the output should be: 1,3,5,7,9

a = input("Enter sequence: ")

print(*[int(i) for i in a.split(',') if int(i)%2!=0],sep=',')



#Question: Write a program that computes the net amount of a bank account based a transaction log from console input.
# The transaction log format is shown as following: D 100 W 200
#D means deposit while W means withdrawal. Suppose the following input is supplied to the program: D 300 D 300 W 200 D 100
# Then, the output should be: 500

a=input("Enter sequence ")

b=a.split()
sum=0
for i in range(len(b)):
    if b[i] == 'D':
        sum+= int(b[i+1])
    elif b[i] == 'W':
        sum = sum-int(b[i+1])
    else:
        pass
print(sum)

#Question: A website requires the users to input username and password to register.
# Write a program to check the validity of password input by users. Following are the criteria for checking the password:

#   At least 1 letter between [a-z]
#   At least 1 number between [0-9]
#    At least 1 letter between [A-Z]
#    At least 1 character from [$#@]
#    Minimum length of transaction password: 6
#    Maximum length of transaction password: 12 Your program should accept a sequence of comma separated passwords and
#    will check them according to the above criteria. Passwords that match the criteria are to be printed, each
#    separated by a comma. Example If the following passwords are given as input to the program: ABd1234@1,a F1#,2w3E*,2We3345
#    Then, the output of the program should be: ABd1234@1

a = input("Enter Sequence: ")
b = a.split(',')



for i in b:
    if len(i)>5 & len(i)<13:
        u = 0
        l = 0
        s = 0
        n = 0

        for j in i:
            if j.isupper():
                u+=1
            elif j.islower():
                l+=1
            elif j.isdigit():
                n+=1
            elif j in ['$','#','@']:
                s+=1
            else:
                pass

        if (u>0) & (l>0) & (s>0) & (n>0):
          print(i)


#Question: You are required to write a program to sort the (name, age, height) tuples by ascending order where name is
# string, age and height are numbers. The tuples are input by console. The sort criteria is: 1: Sort based on name; 2:
# Then sort based on age; 3: Then sort by score. The priority is that name > age > score. If the following tuples are
# given as input to the program: Tom,19,80 John,20,90 Jony,17,91 Jony,17,93 Json,21,85 Then, the output of the program
# should be: [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

a = input("Enter sequence: ")
b= a.split()

lst=[]
for i in (sorted(b)):
    lst.append(tuple(i.split(',')))
print(lst)

#Question: Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

def div(n):
    for i in range (0,n+1):
        if i%7==0:
            yield (i)

a = div(100)

print(next(a))
print(next(a))
print(next(a))


