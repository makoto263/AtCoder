n,m=map(int,input().split())
b=list(map(int, input().split()))
w=list(map(int, input().split()))

b_large = sorted([x for x in b if x > 0], reverse=True)
w_large = sorted([x for x in w if x > 0], reverse=True)

b_small = sorted([y for y in b if y < 0], reverse=True)
w_small = sorted([y for y in w if y < 0], reverse=True)

count=0
count2=0

k=len(b_large)
l=0
                

for i in range(len(b_large)):
        count+=b_large[i] #bの自然数を全て足す
        
if len(b_large)<len(w_large): #もしもbの自然数の数よりwの自然数の数が大きかった場合
    for j in range(len(b_large)): #bの自然数の数だけwの自然数を足す（大きい順）
            count+=w_large[j]
            count2=count
            
    while k<len(w_large) and l<len(b_small): #b_small[0]とw_large[len(b_large):](wの自然数以降のw_large)を足した数がcountより大きかったら増やす
        newcount=count2+w_large[k]+b_small[l]
        if newcount>count2:
            count2=newcount
        k+=1
        l+=1
        
else:
    for j in range(len(w_large)): #もしもbの自然数の方が大きかったらbとwの自然数を全て足す
        count+=w_large[j]


if count2>count:
    print(count2)
else:
    print(count)

