'''
l=[2,]
for i in range (2,21):
    for j in range (2,20):
        if i%j == 0:
            break
        else :
            l.append(i)
print(list(set(l)))

print([x for x in range(2, 20) if all(x % y != 0 for y in range(2, x))])

print([i for i in range (1,101) if i%2==0 and i%5==0 ])
a = [(n,'divisible' )if n%3 == 0 else (n,'not divisible') for n in range(1,11)]
print(a)


A=[[1,2,3],[2,3,1]]
B=[[2,3,5],[3,6,7],[8,6,7]]


final = []
for i in range(len(A)):
    add = []
    for j in range(len(B[0])):
        l = []
        for k in range(len(B)):
            mul = A[i][k] * B[k][j]
            l.append(mul)

        add.append(sum(l))
    final.append(add)

print (final)
'''
with open("sorted_data1.txt") as t:
      t.read()