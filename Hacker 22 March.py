'''
#1 Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line
# with  digits after the decimal. The function should not return a value.

def plusMinus(arr):
    # Write your code here
    p = 0
    z = 0
    n = 0
    for i in arr:
        if i > 0:
            p += 1
        elif i == 0:
            z += 1
        else:
            n += 1
    print(round(p / (p + z + n), 6))
    print(round(n / (p + z + n), 6))
    print(round(z / (p + z + n), 6))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

#2Print two space-separated integers on one line: the minimum sum and the maximum sum of  of  elements.
def miniMaxSum(arr):
    # Write your code here
    s = sum(arr)
    m= sum(arr)-max(arr)
    mx= sum(arr)-min(arr)
    print (m,mx)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))






def timeConversion(s):
    # Write your code here
    l = s.split(':')
    r = []
    if "PM" in s:
        for i in l:
            if len(i) == 4:
                r.append(i[:2])
            elif l.index(i) == 0:
                if i == '12':
                    r.append(i)
                else:
                    r.append(str(int(i) + 12))
            else:
                r.append(i)
        print(':'.join(r))
    else:
        for i in l:
            if len(i) == 4:
                r.append(i[:2])
            elif l.index(i) == 0:
                if i == '12':
                    r.append(str(int(i) - 12)+'0')
                else:
                    r.append(i)
            else:
                r.append(i)
        print(':'.join(r))
s="12:05:45AM"
timeConversion(s)
'''

# Fibonacchi number:

# 0, 1, 1, 2, 3, 5, 8, 13 , 21, 34

'''
a= 0
b= 1

for i in range (10):
    c= a+b
    print(a, end=' ')
    a=b
    b=c


def fib(n):
    if n == 0:
        return 0
    elif n == 1 :
        return 1
    else:
        return fib(n-1) + fib(n-2)

for i in range (10):
    print(fib(i), end=" ")
'''
def count_substring(string, sub_string):
    c=0
    for i in range(0,len(string)-len(sub_string)+1):
        s=''
        for j in range(0,len(sub_string)):
             s+= string[i+j]
        if s == sub_string:
             c+=1
        else:
            print(string[:i+3])
    return c
print(count_substring("ABCDCDC","CDC"))