#A_StatursCode
'''
S=int(input())

if 200<=S<=299:
    print("Success")

else:
    print("Failure")

#B_Unauthorized
N=int(input())
S=[]
count=0
login_check=False

for i in range(N):
    S.append(input())

for i in range(len(S)):
    if S[i]=='login':
        login_check=True
    elif S[i]=='logout':
        login_check=False
    elif S[i]=='private':
        if not login_check:
            count+=1

print(count)

#C
N, K = map(int, input().split())
A=[1]*K
mdo=10**9

for i in range(K,N+1):
    count=sum(A[i-K:i])
    A.append(count%10**9)

print(A[N])
'''

