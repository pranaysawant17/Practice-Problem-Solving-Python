'''
# Q11. Write a program to display the largest word from the string.

s = input("Enter String: ")
print(sorted(s.split(),key=len)[-1], len(sorted(s.split(),key=len)[-1]))

print()

l=[]
for i in s.split():
    l.append(len(i))
for j in s.split():
    if len(j)==max(l):
        print(j)


str=input("Enter any String :")
L = str.split()
max=0
b=""
for i in L:
     if len(i) > max:
           b=i
           max=len(i)
print("Longest word is ",b)


#Q12. Write a program to accept a string and display it in upper case.
s= input("Enter String: ")
print(s.upper())



#Q13. Write a program to display the unique words from the string.

s= input("Enter String: ")


print(list(set(s.split())))


#Q14. Write a program to accept a string and display the ascii value of each character.

s= input("Enter String: ")

print([(i, ord(i)) for i in s])



# Q15. Write a program to accept a string and replace all spaces by ‘#’ symbol.
s= input("Enter String: ")

a= s.split()

print('#'.join(a))

print(s.replace(' ','#'))


#Q16. Write a program to accept two strings from the user and display the common words.(Ignore case)

s1= input("Enter String: ")
s2= input("Enter String: ")

set1= set(s1.lower().split())
set2 = set(s2.lower().split())

print (set1.intersection(set2))

#Q17. Write a program to accept a string and count the frequency of each vowel.

s1 = input(" Enter Sting: ")

d = {}
for i in ['a','e','i','o','u']:
    d[i] = s1.lower().count(i)

print(d)

print({i:s1.lower().count(i) for i in ['a','e','i','o','u'] })

#Q18. Write a program to display the smallest word from the string.
s1 = input("Enter String: ")
l=[]
for i in s1.split():
    l.append(len(i))
for j in s1.split():
    if len(j) == min(l):
        print(j)


#Q19. Write a program to accept a string and display the string in Title case. (first alphabet of each word in upper case)
s1 = input("Enter String: ")
print(s1.title())


# Q20. Write a program to accept a string and display the string with changed case.(Change upper case alphabet to lower
# case and vice versa)

s1 = input("Enter String: ")
print(s1.swapcase())

'''
k=1
d=0
for i in range(1,5):
    #c=0
    for j in range(k, d,-1):
        print(j, end=' ')
        #c+=1
    print()
    k=k+i+1
    d+=i

print([i for i in range(3,1,-1)])


k = 1
m = 1
for i in range(1, 5):
    m = k + i - 1
    for j in range(1, i+1):
        if(i % 2 == 1):
            print(k, end=" ")
        else:
            print(m, end=" ")
            m -= 1
        k += 1
    print()