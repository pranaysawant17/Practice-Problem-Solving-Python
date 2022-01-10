'''
def max_number (x,y,z):
    if (x>y and x>z):
        return x
    elif (y>x and y>z):
        return y
    else:
        return z

print(max_number (17, 11 ,13))


def list_sum(a):
    sum = 0
    for i in a:
        sum=sum + i
    return sum
print(list_sum((12,5,17,9)))


def list_mul(a):
    mul = 1
    for i in a:
        mul *= i
    return mul
print(list_mul((12,5,17,9)))

def div(a):
    k=[]

    for i in range(1,a):
        if a % i == 0:
            k.append(i)
    return k



def sum_div(a):
    lst=div(a)
    sum=0
    for i in lst:
        sum=sum+i
    return sum

def num_com(a):
    if sum_div(a) == a:
        return a
    else:
        return ("no perfect num")
print(sum_div(14))

strng= input("Enter String: ")
length= 0
for i in strng:
    length+=1
print ("Length of string: ", length)

a = input("Enter String: ")

dict={}
for i in a:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)

a = input("Enter String: ")

dict={}

for key in a:
    dict[key]=dict.get(key,0)+1
print(dict)

s=input("Enter string: ")
e= []
for i in s:
    e.append(i)
e[0]=s[-1]
e[-1]=s[0]
d="".join(e)
print(d)

s='my name'
cnt=0
for i in s:
    print(i,"index is", cnt)
    cnt+=1
class ho:
    def __init__ (will, name, account):
        will.name = name
        will.account =account
    def show (will):
        print(will.name,will.account)
h=ho ("pranay",123)
h.show()
'''
s = 'Kun#$ dan'
s=s.split('#$')
print(s)
''.join(s)
print(s)