'''
#[1] With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
#Suppose the following input is supplied to the program:
n= int(input("Enter number: "))
print({i : i **2 for i in range(1, n+1)})

#[2]Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
#Suppose the following input is supplied to the program:
#34,67,55,33,12,98
#Then, the output should be:
#['34', '67', '55', '33', '12', '98']
#('34', '67', '55', '33', '12', '98')


print([x for x in input("Enter numbers: ").split(',')])
print(tuple(x for x in input("Enter numbers: ").split(',')))


#[3]Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
#Suppose the following input is supplied to the program:
#without,hello,bag,world
#Then, the output should be:
#bag,hello,without,world

print(','.join(sorted([x for x in input("Enter string: ").split(',')])))


#[4]Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

print(sum([int(i) for i in(input("Enter numbers: ").replace('a','9')).split('+')]))

#[5] please write a program to print the list after removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

a=[12,24,35,70,88,120,155]
print([i  for i in a if i%35 !=0])


#[1]Python Program to remove the duplicate items from a List.
lst = [1,1,2,3,3,3,'a','a']
print(list(set(lst)))

#[2]Python Program to Read a List of Words and Return the length of the Longest One.
words = ['ab', 'Green', 'read', 'prime']
print(max(len(i) for i in words))

#[3]Python program to remove the ith Occurrence of the Given Word in a list where Words can Repeat.

words = ['ab', 'Green', 'read', 'prime', 'ab','dr','ab']
new =[]
c=0
for i in words :
    if i == 'ab':
        c+=1
        if c==2:
            pass
        else:
            new.append(i)
    else:
        new.append(i)
print(new)
#solution 2
l = ['Red', 'Blue', 'Yellow', 'Red', 'Yellow', 'Red']
n = int(input("Enter the number:"))
l1 = []
for i in l:
    if i == l[n]:
        continue
    l1.append(i)
print(l1)

#[4]Write a Python program to append a list to the second list.
l = ['Red', 'Blue', 'Yellow', 'Red', 'Yellow', 'Red']

new = [i for i in l]
print(new)

new1= l.copy()
print(new1)

#[5]Write a Python Program to select an item randomly from a list.
import random
l = ['Red', 'Blue', 'Yellow', 'Red', 'Yellow', 'Red']
print(random.choice(l))

#Write a Python Program to check whether two lists are circularly identical.

a=[1,2,3,4]
b=[1,2,3,"c"]

lst=[]
for i in a:
    if i in b:
        lst.append(True)
    else:
        lst.append(False)
for j in b:
    if j in b:
        lst.append(True)
    else:
        lst.append(False)
if all(lst)== True:
    print("List are identical")
else:
    print("List are not identical")
# solution 2
l = [10, 10, 0, 0, 10]
l1 = [10, 10, 10, 0, 1]
l2 = ''.join(map(str, l1)) in ''.join(map(str, l * 2))
print(l2)


#Write a Python Program to check whether the given number in a list is anagram or not.

s= 'python'
s1= 'thonpn'

print( (sorted([i for i in s1])) == (sorted([j for j in s])))

# Write a Python program to convert a list of multiple integers into a single integer.

a = [21, 22 ,23]
x = int("".join(map(str, a)))
print(x)
y = int("".join([str(i) for i in a]))
print(y)

'''





