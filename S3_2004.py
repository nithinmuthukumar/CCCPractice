from string import ascii_uppercase
from collections import defaultdict
from queue import Queue
from pprint import pprint
grid=[[0 for i in range(9)] for i in range(10)]
indegree=[[0 for i in range(9)] for i in range(10)]
d=defaultdict(list)
queue=Queue()  
for y in range(10):
    row=[i.split("+") for i in input().split()]

    for x in range(9):
        
        if not row[x][0].isdigit():
            
            indegree[y][x]=len(row[x])
            for i in row[x]:
                d[(ord(i[0])-ord('A'),int(i[1])-1)].append((y,x))
        else:
            grid[y][x]=int(row[x][0])
            queue.put((y,x))
    
visited=set()
while not queue.empty():
    cell=queue.get()
    for c in d[cell]:
        if c not in visited:
            indegree[c[0]][c[1]]-=1
            grid[c[0]][c[1]]+=grid[cell[0]][cell[1]]
            if indegree[c[0]][c[1]]==0:
                visited.add(c)
                queue.put(c)
                
for y in range(10):
    for x in range(9):
        if indegree[y][x]:
            grid[y][x]='*'
print("\n".join([' '.join([str(s) for s in i]) for i in grid]))

        
