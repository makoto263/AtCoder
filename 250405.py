#A-ABC200Party
'''
A=int(input())

if 400%A==0:
    print(400//A)

else:
    print(-1)

#B-Sum of Geometric Series
A,M=map(int,input().split())
Z=0

for i in range(M+1):
    Z+=pow(A,i)
    if Z>pow(10,9):
        print("inf")
        exit()

print(Z)
'''
#C-2^ab^2

N=int(input())
count=set()

for i in range(1,60):
    pow1=2**i
    if pow1>N:
        break
    else:
        max_j=int((N//pow1)**0.5)+1
        for j in range(1,max_j+1):
            Z=pow1*j*j
            if Z>N:
                break
            else:
                count.add(Z)

print(len(count))   








    

