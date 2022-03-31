'''
from functools import reduce

list1 = [2,7,8,9,12]

print(reduce(lambda x,y: x+y,list1))
print(reduce(lambda x,y: x*y, list1))
print(reduce(lambda x,y: max(x,y), list1))
print(reduce(lambda x,y: x+y, list1,20))



from functools import total_ordering
@total_ordering
class car:
    def __init__(self, model, price):
        self.model=model
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __lt__(self, other):
        return self.price < other.price


c1 = car("Tata",700 )
c2 = car ('Honda',800 )

print( c1 >= c2)
#print(c1.model == c2.model)
#print(c1.price == c2.price)
#print(c1.passanger<c2.passanger)


from functools import lru_cache

@lru_cache(maxsize=2)
def fib(n):
    if n<2:
        return n
    print("fib num",n)

    return fib(n-1)+fib(n-2)




print([fib(i) for i in range(10)])

print(fib.cache_info())

def mul(a,b):
    return a*b
from functools import partial
mula_one = partial(mul,8)

print(mula_one(7))
'''

import time
from  functools import cache

@cache
def fib(n):
    if n<2:
        return n


    return fib(n-1)+fib(n-2)


print(time.time(),fib(10), time.time())
print(time.time(),fib(15), time.time())
print(time.time(),fib(10), time.time())



from functools import partial

pow_2 = partial(pow, exp=2)

print(pow_2(5))