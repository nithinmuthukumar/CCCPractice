from functools import reduce
from pprint import pprint
import math
n=int(input())
mats=[]
for i in range(n):
    r,c=[int(i) for i in input().split()]
    mats.append([[int(i) for i in input().split()] for i in range(r)])
ans=mats.pop()
max_element=-math.inf
min_element=math.inf
while mats:
    m1=mats.pop(0)
    m2=ans
    m=len(m2)
    p=len(m1)
    n=len(m2[0])
    q=len(m1[0])
    ans=[]
    for y in range(m*p):
        ans.append([])
        for x in range(n*q):
            ans[y].append(m2[y%m][x%n]*m1[y//m][x//n])
for y in ans:
    for x in y:
        max_element=max(max_element,x)
        min_element=min(min_element,x)
rows=[sum(i) for i in ans]
columns=[sum(i) for i in zip(*ans)]
print(max_element)
print(min_element)
print(max(rows))
print(min(rows))
print(max(columns))
print(min(columns))

    
    
    
    
    
    
        
