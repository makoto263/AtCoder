'''
#ABC086C
N=int(input())

t,x,y=[0],[0],[0]
for i in range(N):
    ti,xi,yi=map(int,input().split())#最初から配列として格納されるわけではない
    t.append(ti)
    x.append(xi)
    y.append(yi)

for i in range(N):
    time=t[i+1]-t[i]
    dist = abs(x[i + 1] - x[i]) + abs(y[i + 1] - y[i])

    if dist>time or (time-dist)%2!=0:
        print("NO")
        exit()

print("YES")

N=int(input())
A=list(map(int,input().split()))

for i in range(N-1):
    if A[i]>A[i+1]:
        print("NO")
        exit()

print("YES")

N=int(input())
S=[]

for i in range(N):
    S.append(input())
for i in range(N):
    for n in range(i+1,N):
        if len(S[i])>len(S[n]):
            tmp=S[i]
            S[i]=S[n]
            S[n]=tmp
print("".join(S))

A=input()
Aprint=[]
for char in A:
    if char=="2":
        Aprint.append(char)
print("".join(Aprint))
       
A=input()
Slist=list(A)

while True:
    change=False
    i=0
    for i in range(len(Slist)-1):
        if Slist[i]=="W" and Slist[i+1]=="A":
            Slist[i]="A"
            Slist[i+1]="C"
            change=True
            break
        
    if change==False:
        print("".join(Slist))
        exit()
'''        
        
    









        
    
