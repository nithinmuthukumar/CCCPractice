from collections import defaultdict
n=int(input())
g=defaultdict(list)
for i in range(n):
    x,y=(int(a) for a in input().split())
    g[x].append(y)
while True:
    v=-1
    x,y=(int(a) for a in input().split())
    
    if x==0 and y==0:
        break
    queue=[(x,-1)]
    visited=set()
    while queue:
        cur=queue.pop(0)
        if y==cur[0]:
            v=cur[1]
            
        for i in g[cur[0]]:
            if i not in visited:
                visited.add(i)
                queue.append((i,cur[1]+1))
    if v==-1:
        print("No")
    else:
        print(f"Yes {v}") 
        
            
                
                
                
                
            
    

    
    
    
    


    
    
    
