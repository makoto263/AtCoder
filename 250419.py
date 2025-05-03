'''
#A_CBC
S=input()
output=[]

for i in S:
    if i.isupper():
        output.append(i)

print("".join(output))

#B_Restaurant Queue

S=int(input())
num=[]
menu=[]

for i in range(S):
    inputs=input().split()
    if inputs[0]=='1':
        num.append(int(inputs[1]))
    elif inputs[0]=='2':
        menu.append(num.pop(0))
for item in munu:
    print(item)
'''
#C_Dislike Foods

N,M=map(int,input().split())
arrays=[]
can_eat=[]

for i in range(M):
    arr=list(map(int,input().split()))
    arrays.append(set(arr[1:]))#最初の数字は食材使用数＝配列には必要ない

    
like_food=list(map(int,input().split()))
                  
for j in range(len(like_food)):
    for arr in arrays:
        if like_food[j] in arr:
            arr.remove(like_food[j])
    can_eat.append(M-len(arrays))
                  
for item in can_eat:
    print(item)
