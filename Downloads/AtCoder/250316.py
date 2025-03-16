
#0215B
S=input()
s=list(S)
count=0

for i in range(len(s)):
    chek=0
    while chek<2:
        if s[i]=="A":
            chek+=1
            for n in range(i+1,len(s)):
                if s[n]=="B":
                    chek+=1
                    for m in range(n+1,len(s)):
                        if s[m]=="C":
                            if n-i==m-n:
                                count+=1
        else:
            break
print(count)

'''

S=input()
N=len(S)
count=0

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+i,N):
            if j-i==k-j and s[i]=="A" and s[j]=="B" and s[k]=="C":　
            #j-i==k-jは条件
                count+=1

print(count)
'''            
