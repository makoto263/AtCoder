'''
#A_NotFound
s=input()
for i in 'abcdefghijklmnopqrstuvwxyz':
    if i not in s:
        print(i)
        break
'''
#B_GridRotation
N=int(input())
S=[]
T=[]

for i in range (N):
    S.append(list(input()))
for j in range (N):
    T.append(list(input()))

def rotate(grid):
    return[list(row) for row in zip(*grid[::-1])]#行を逆順にする(grid[::1])->列と行の入れ替えzip(*)->配列にする

min_operations=float('inf')#float('inf')=無限　最初に無限にしておく事で31行目で必ず更新される
current=S

for k in range(4):
    diff=0
    for i in range(N):
        for j in range(N):
            if current[i][j]!=T[i][j]:
                diff+=1
    min_operations=min(min_operations,diff+k)#diff=色を変更する回数 k=回転数
    current=rotate(current)

print(min_operations)
    
    
 
