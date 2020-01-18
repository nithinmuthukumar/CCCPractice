def find_sq(x,y,m):
    if m==1:
        if ((5**m//x in [1,2,3]) and y**m//y==0) or (5**m//x==2 and y**m//y=1):
            return True
    m-=1
    return find_sq(x-5**m,y-5**m,m) or find_sq(x-2*5**m,y-2*5**m,m) or find_sq(x-3*5**m,y-5**m,m)
    
t=int(input())
for i in range(t):
    m,x,y=[int(w) for w in input().split()]
    print(find_sq(x,y,m))



