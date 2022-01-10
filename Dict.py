'''
dict1= {3:1, 4:23, 5:56,7:16}
sum=0
for i ,j in (dict1.items()):
    sum+=i + j
print (sum)

dict1= {3:1, 4:23, 5:56,7:16}
dict2= {6:1, 11:23, 15:56,13:16}
dict1.update(dict2)

print(dict1)
dict1= {3:1, 4:23, 5:56,7:16}
print
for i ,j in (dict1.items()):
    lst.append([i,j])
print(lst)

def odd_num(a):
    if a%2 != 0:
        return True
    else:
        return  False
def num_series(*args):
    l=[]
    for i in args:
      l.append(odd_num(i))
    if l.count(True)>=2:
        return True
    else:
        return False

print(num_series(2,4,7,8,9))
print(num_series(1,2,6,8,10))
print(num_series(1,2,3,4,5))



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                    break


twoSum (List[2,7,11,15],9)
'''