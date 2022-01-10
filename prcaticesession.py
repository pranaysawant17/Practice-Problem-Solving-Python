'''
a = int(input("number:"))

add = 1
i = 1
while i < (a+1):
    add = add + i
    print (add)
    i+=1

str = "a4k3b2"
ans=''

for i in str:
    if i.isalpha():
        ans+= i
        b=i
    else:
       j=int(i)
       ans=ans + chr(ord(b)+j)
print(ans)


b= 'a123'
a=[]
for i in b:
    if i.isalpha():
     a.append(i)
    else:
        a.append(int(i))
print(sorted(a))




st= 'apllegreen'
dict={}

for key in st:
    dict[key]=dict.get(key,0)+1
print(dict)
'''

'''
a= 'python'
b='GREATESTVER'
ans=''

i=j=0

while i<len(a)and j<len(b):
    ans= ans+a[i]+b[j]
    i+=1
    j+=1
if len(a)>len(b):
    for i in range(len(b),len(a)):
        ans= ans+a[i]
else:
    for i in range(len(a),len(b)):
        ans= ans+b[i]
print(ans)

ans=''
for (i in range(len(a))) and (j in range(len(b))):
    ans= ans+a[i]+b[i]
print(ans)


st="GA954rick654"

apl=[]
num=[]

for i in st:
    if i.isalpha():
        apl.append(i)
    else:
        num.append(i)

print(''.join(sorted(apl, key=lambda x:x.lower())+sorted(num)))


from  collections import  Counter

s = "applepie"
a=Counter(s)
print (a)

b= {}

for i in s:
    b[i]= s.count(i)
print(b)


print({ i: s.count(i) for i in s})

'''