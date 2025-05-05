'''
#P25
N=int(input())
print(N*N)

#P27
A,B=map(int,input().split())
print(A+B)

#P28
N,X=map(int,input().split())
A=list(map(int,input().split()))

for i in range(len(A)):
    if A[i]==X:
        print("Yes")
        exit()
print("No")

#P30
A,B=map(int,input().split())
for i in range(A,B+1):
    print(i)
    if 100%i==0:
        print("Yes")
        exit()
print("No")

#P31
N,K=map(int,input().split())
red_card=list(map(int,input().split()))
blue_card=list(map(int,input().split()))

for i in range(N):
    for j in range(N):
        if red_card[i]+blue_card[j]==K:
            print("Yes")
            exit()
print("No")

#P33
N=int(input())
goods=list(map(int,input().split()))

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if goods[i]+goods[j]+goods[k]==1000:
                print("Yes")
                exit()
print("No")

#P34
N=int(input())
binary=[]
num=N

while num=!0:
    binary.append(num%2)
    num=num//2

while len(binary)<10:
    binary.append(0)
    
print(''.join(map(str, binary[::-1])))

#P38
N=list(map(int,input()))
binary=N[::-1]
num=0

for i in range(len(binary)):
    num+=binary[i]*(2**i)

print(num)
'''
N,K=map(int,input().split())
count=0

for card_1 in range(1,N+1):
    for card_2 in range(1,N+1):
        card_3=K-card_1-card_2
        if card_3>=1 and card_3<=N:
            count+=1
            
print(count)





