n,m=map(int,input().split())
a=list(map(int, input().split()))
fullnum=[]

for i in range(1,n+1):
    fullnum.append(i)
    
for i in range(len(a)):
    for j in range(len(fullnum)):
        if a[i]==fullnum[j]:
            fullnum.pop(j)
            break

print(len(fullnum))
print(" ".join(map (str, fullnum)))
            
    
    
    
