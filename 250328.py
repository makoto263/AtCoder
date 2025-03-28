#B Heavy Snake
A=list(map(int,input().split()))
N,D=A[0],A[1]

snake=[]

for i in range(N):
    T, L = map(int, input().split())
    snake.append([T,L])

for k in range(1,D+1):
    heavy=[]
    
    for i in range(N):
        T=snake[i][0]
        L=snake[i][1]+k
        heavy.append(T*L)

    print(max(heavy))
        
