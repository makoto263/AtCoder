'''
#A
x=input()
temp=float(x)

if temp>=38.0:
    print("1")
elif 37.5<=temp and temp<=38.0:
    print("2")
else:
    print("3")

#B
x=input()
s=list(x)
count=0
i=0

while i<len(s):
    if (i+1)%2==1: #奇数の時
        if s[i]!="i":
            s.insert(i,"i")
            count+=1
    else: 
        if s[i]!="o":
            s.insert(i,"o")
            count+=1
    i+=1

if len(s)%2==1:
    count+=1

print(count)

#C
N=int(input())
A=input()
a=list(A)
x=[]
y=[]
num=[]

for i in range(N):
    slash_x=a[:i]
    slash_x=sorted(slash_x)
    slash_y=a[i:]
    slash_y=sorted(slash_y)
    x=[]
    y=[]
    for i in range(len(slash_x)):
        if slash_x[i]!=slash_x[i+1]:
            x.append(slash_x[i])
    for i in range(len(slash_y)):
        if slash_y[i]!=slash_y[i+1]:
            y.append(slash_y[i])
    num.append(len(x)+len(y))

num=sorted(num,reverse=True)
print(num[0])
'''           
            
N=int(input())
A=input()
a=list(map(int, A.split()))
num=[]

for i in range(1,N):
    x=set(a[:i])
    y=set(a[i:])
    num.append(len(x)+len(y))

print(max(num))



















            


