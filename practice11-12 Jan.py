#1 check if substring is present in given string.
s = "geekgeekss"
a = "ab"


while a in s:
   i = s.index(a)

   y = s[:i] + s[i+len(a):]
   s=y
else:
    if len(s)>0:
      print("No")
    else:
        print("Yes")


#2.Sort String list by K character frequency
s= ["apple" , "peeech" , "loop", "polee"]

print(sorted(s, key = lambda x: x.count("e") , reverse= True))
print(sorted(s, key = lambda x: x.count("e")))


#3 Remove punctuation from string
s=''
a= "abcd#$$def$$g"

for i in a:
    if i.isalpha():
        s+=i
print(s)


#4 Retain records with N occurrences of K

a = [(4, 5, 5, 4), (5, 4, 3)]
K = 5
N = 2
c=[]
for i in range(len(a)):
   if a[i].count(K) == N:
       c.append(a[i])
print(c)

n=8
i=1
while i < 8:
    print(' '*(n-i)+"*"*i+"*"*i+    ' '*(n-i))
    i+=1


#5 Print index of element in list whose sum is equal to the target.
def twosum( num , target):
    for i in range(len(num)):
        for j in range(i+1, (len(num))):
            if num[i] + num[j] == target:
                return [i,j]
print(twosum([2,7,11,15],9))


#6 Reverse the given list , add them element wise and reverse the output

def number(a):
    s=''
    for i in a:
        s += str(i)
    s=s[::-1]
    return int(s)

def lst_add(lst1,lst2):
    ans_lst=[]
    add=number(lst1) + number(lst2)
    for i in str(add):
        ans_lst.append(int(i))
    return ans_lst[::-1]
print (lst_add([2,4,3], [5,6,4]))
print(lst_add([9,9,9,9,9,9,9],[9,9,9,9]))

'