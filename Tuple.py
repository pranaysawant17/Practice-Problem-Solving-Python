
#1. Write a Python program to create a tuple
t=()
tu=tuple()
print(type (t))
print(type(tu))

#2 Write a Python program to create a tuple with different data types

a = (1, 'a', 'b', 2)
print(a)
print(type(a))

#3. Write a Python program to create a tuple with numbers and  one item
a = (1, 2, 3, 4)
b = (5,)
print(a)
print(b)


#4. Write a Python program to unpack a tuple in several variables
a, b, c, d = (1, 'a', 3, 'b')
print(a ,b, c, d)

#5. Write a Python program to add an item in a tuple
# We cannot add item in tuple as they are immutable.
# We can merge two tuples.
a= (1, 2, 3)
b=(5, 6)
c= a+b
print(c)
# We can convert tuple to list and append item.
new_a=list(a)
new_a.append(7)
a=tuple(new_a)
print(a)


#6. Write a Python program to convert a tuple to a string
a = (1 ,'a', 'c', 5)
list_a = list(a)
print (list_a, type(list_a))


#7. Write a Python program to get the 4th element and 4th element from last of a tuple

a = (11 ,15 ,17, 'f', 'g', 'l', 'p', 8, 9, 10)
print(a[3])
print(a[-4])



#8. Write a Python program to create the colon of a tuple
a = (':',)
print(type(a))


#9. Write a Python program to find the repeated items of a tuple
a = (1, 1, 2, 'a', 'b', 'b', 5, 6, 9, 5 )
b= []
for i in a:
    if a.count(i)>1:

        if i not in b:
            b.append(i)
            print(i, "count is :" ,a.count(i))


#10. Write a Python program to check whether an element exists within a tuple
a = (1, 1, 2, 'a', 'b', 'b', 5, 6, 9, 5 )
print(3 in a)


#11. Write a Python program to convert a list to a tuple
lst = [ 1, 'd', 'b', 2]
tup = tuple(lst)
print(tup)


#12. Write a Python program to remove an item from a tuple
# We cannot remove item from tuple directly as it is immutable.
# We can convert it to list  or slicing to make a new tuple without that item.

a = (1 , 2, 3, 4)
# remove 2
c = a[:1] + a[2:]
print (c)

lst_a= list(a)
lst_a.remove(2)
print (tuple(lst_a))



#13. Write a Python program to slice a tuple
a = (1 , 2, 3, 4)
print(a[:2])


#14. Write a Python program to find the index of an item of a tuple
a = (1 , 2, 3, 4)
print(a.index(2))

#15. Write a Python program to find the length of a tuple
a = (1 , 2, 3, 4)
print (len(a))


#16. Write a Python program to convert a tuple to a dictionary
a = ((1 , 2) ,(3, 4))
print(dict(a))
print (dict((y,x) for x,y in a))


#17. Write a Python program to unzip a list of tuples into individual lists
a = ((1 , 2) ,(3, 4))
b=[]
for i,j in  a:
    b.append(i)
    b.append(j)
print (b)




#18. Write a Python program to reverse a tuple

a= (1 , 2,  3, 4)
print(a[::-1])
print(tuple(reversed(a)))





#20. Write a Python program to print a tuple with string formatting.
#Sample tuple : (100, 200, 300)
#Output : This is a tuple (100, 200, 300)

a =(100, 200, 300)
print("This is tuple",str(a))



#21. Write a Python program to replace last value of tuples in a list.
#Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
#Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
a= [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
b=[]
for i in a:
    c= i[:2]+(100,)
    b.append(c)
print(b)

#22. Write a Python program to remove an empty tuple(s) from a list of tuples. Go to the editor
#Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
#Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
a = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
b=[]
for i in a:
    if i != ():
        b.append(i)
print (b)


#23. Write a Python program to sort a tuple by its float element. Go to the editor
#Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
#Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]
a = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
print(sorted(a, key = (lambda x : float(x[1]) ), reverse= True))


#Write a Python program to count the elements in a list until an element is a tuple
a =[1, 2, 3, 4, (1,2), 5, 6]
count=0
for i in a:
 if type(i) == tuple:
     break
 else:
    count += 1
print(count)

#25. Write a Python program convert a given string list to a tuple.
#Original string: python 3.0
#<class 'str'>
#Convert the said string to a tuple:
#('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
#<class 'tuple'>

a= 'python 3.0'
b=tuple([i for i in a])
print(b, type(b))


#26. Write a Python program calculate the product, multiplying all the numbers of a given tuple. Go to the editor
#Original Tuple:
#(4, 3, 2, 2, -1, 18)
#Product - multiplying all the numbers of the said tuple: -864
#Original Tuple:
#(2, 4, 8, 8, 3, 2, 9)
#Product - multiplying all the numbers of the said tuple: 27648

a= (4, 3, 2, 2, -1, 18)
mul1=1
for i in a:
    mul1*=i
print(mul1)

b = (2, 4, 8, 8, 3, 2, 9)
mul2=1
for i in b:
    mul2*=i
print(mul2)


#27. Write a Python program to calculate the average value of the numbers in a given tuple of tuples. Go to the editor
#Original Tuple: ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
#Average value of the numbers of the said tuple of tuples: [30.5, 34.25, 27.0, 23.25]
#Original Tuple: ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
#Average value of the numbers of the said tuple of tuples: [25.5, -18.0, 3.75]
a = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))

def average_tuple(nums):
    result = [sum(x) / len(x) for x in zip(*nums)]
    return result

nums = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
print ("Original Tuple: ")
print(nums)
print("\nAverage value of the numbers of the said tuple of tuples:\n",average_tuple(nums))

nums = ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
print ("\nOriginal Tuple: ")
print(nums)
print("\nAverage value of the numbers of the said tuple of tuples:\n",average_tuple(nums))

#28. Write a Python program to convert a tuple of string values to a tuple of integer values. Go to the editor
#Original tuple values: (('333', '33'), ('1416', '55'))
#New tuple values: ((333, 33), (1416, 55))

a = (('333', '33'), ('1416', '55'))
b=tuple((int(x),int(y)) for x,y in a )
print(b)


#29. Write a Python program to convert a given tuple of positive integers into an integer.
#Original tuple: (1, 2, 3)
#Convert the said tuple of positive integers into an integer: 123
#Original tuple:(10, 20, 40, 5, 70)
#Convert the said tuple of positive integers into an integer:102040570

def integer_tup(a):
    st_r=[]
    for i in a:
        st_r.append(str(i))
    return int(''.join (st_r))
i=(1, 2, 3)
print(integer_tup(i))
j=(10, 20, 40, 5, 70)
print(integer_tup(j))

#30. Write a Python program to check if a specified element presents in a tuple of tuples. Go to the editor
#Original list: (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
#Check if White presenet in said tuple of tuples!
#True
#Check if White presenet in said tuple of tuples!
#True
#Check if Olive presenet in said tuple of tuples!
#False

a=(('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
for i in a:
   if 'Olive' in i:
      print (True)
      break
   else:
      continue
else:
    print(False)


#31. Write a Python program to compute element-wise sum of given tuples. Go to the editor
#Original lists:(1, 2, 3, 4)(3, 5, 2, 1)(2, 2, 3, 1)
#Element-wise sum of the said tuples: (6, 9, 8, 6)
a=(1, 2, 3, 4)
b= (3, 5, 2, 1)
c= (2, 2, 3, 1)
sum_tup= map(lambda x, y,z: x + y + z, a,b,c)

print(tuple(sum_tup))


#32. Write a Python program to compute the sum of all the elements of each tuple stored inside a list of tuples. Go to the editor
#Original list of tuples: [(1, 2), (2, 3), (3, 4)]
#Sum of all the elements of each tuple stored inside the said list of tuples: [3, 5, 7]
#Original list of tuples: [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
#Sum of all the elements of each tuple stored inside the said list of tuples: [9, -1, 7, 8]
a= [(1, 2), (2, 3), (3, 4)]
print(list(map(sum,a)))
b=[(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
print(list(map(sum,b)))

#33. Write a Python program to convert a given list of tuples to a list of lists. Go to the editor
#Original list of tuples: [(1, 2), (2, 3), (3, 4)]
#Convert the said list of tuples to a list of lists: [[1, 2], [2, 3], [3, 4]]
#Original list of tuples: [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
#Convert the said list of tuples to a list of lists: [[1, 2], [2, 3, 5], [3, 4], [2, 3, 4, 2]]
def lst_tup(a):
    lst=[]
    for i in a:
        lst.append(list(i))
    return lst
print (lst_tup([(1, 2), (2, 3), (3, 4)]))
print (lst_tup([(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]))
