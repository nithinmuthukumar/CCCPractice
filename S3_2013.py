t=int(input())
g=int(input())
f=frozenset
games=[f([0,1]),f([0,2]),f([0,3]),f([1,2]),f([1,3]),f([2,3])]
def combs(games,scores,team):
    if not games:
        if scores[team]==max(scores) and scores.count(max(scores))==1:
            return 1
        return 0
        
        
    game=games[0]
    total=0
    for s1,s2 in [(1,1),(0,3),(3,0)]:
        
        cp=scores[:]
        cp[game[0]]+=s1
        cp[game[1]]+=s2
        total+=combs(games[1:],cp,team)
    return total 
    
    
scores=[0,0,0,0]
for i in range(g):
    a,b,s_a,s_b=(int(i) for i in input().split())
    a-=1
    b-=1
    if s_a>s_b:
        scores[a]+=3
    elif s_b>s_a:
        scores[b]+=3
    else:
        scores[a]+=1
        scores[b]+=1
    games.remove(frozenset([a,b]))
    

    
print(combs([list(q) for q in games],scores,t-1))
    
    
