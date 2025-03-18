'''
#ABC086A
a,b=map(int,input().split()) #list(map(int,input().split()))でリストも制作可能
mul=a*b
if mul%2==0:
    print("Even")
else:
    print("Odd")

#ABC081A
a=list(map(int,input()))
sum=0
for i in range(0,3):　#0から３回繰り返すと同じ意味
    if a[i]==1:
        sum=sum+1

print(sum)


#ABC081B
num=int(input()) #map(int,input())にすると一文字ずつ整列してしまう
a=list(map(int,input().split()))
sum=0

while all(x%2==0 for x in a): #allは全ての配列に対して検査可能　x in aはaの中にinが含まれているか
    sum+=1
    for i in range(num):
        a[i]=a[i]/2
    
print(sum)
   
#ABC087B #組み合わせを総当たりする
a=int(input())
b=int(input())
c=int(input())
x=int(input())
sum=0

for A in range(a+1):
    for B in range(b+1):
        for C in range(c+1):
            total=500*A+100*B+50*C
            if total==x:
                sum+=1
print(sum)            

#ABC083B
n,a,b=map(int,input().split())

sum=0;

for i in range(n+1):
    if i<10:
        if a<=i<=b:
            sum+=i
    elif 10<=i<100:
        A=i//10
        B=i%10
        if a<=A+B<=b:
            sum+=i
    elif 100<=i<1000:
        A=i//100
        B=i%100
        C=B//10
        D=C%10
        if a<=A+B+C+D<=b:
            sum+=i
    elif 1000<=i<10000:
        A=i//1000
        B=i%1000
        C=B//100
        D=B%100
        E=D//10
        F=D%10
        if a<=A+B+C+D+E+F<=b:
            sum+=i
    elif 10000<=i<100000:
        A=i//10000
        B=i%10000
        C=B//1000
        D=B%1000
        E=D//100
        F=D%100
        G=F//10
        H=F%10
        if a<=A+B+C+D+E+F+G+H<=b:
            sum+=i
print(sum)

n,a,b=map(int,input().split())
sum=0

for i in range(n+1):
    add=0
    m=i
    if i<10:
        if a<=i<=b:
            sum+=i
    else:
        while m!=0:
            add+=m%10
            m=m//10
        if a<=add<=b:
            sum+=i
print(sum)
            

#ABC088B
n=int(input())
card=list(map(int,input().split()))
card.sort(reverse=True)#降順で並び変える
Alice=0
Bod=0

for i in range(n):
    if i%2==0:
        Alice+=card.pop(0)
    else:
        Bod+=card.pop(0)

print(Alice-Bod)


#ABC085B
n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
motchi=set(a)
print(len(motchi))

#ABC085C
num,yen=map(int,input().split())

for x in range(num+1):
    for y in range(num+1-x):#yの最大値がnum-xに制限される
        z=num-x-y
        if x*10000+y*5000+z*1000==yen:
            print(x, y, z)
            exit()

print(-1,-1,-1)


#ABC049C
s=input()
slist=[]

while len(s)!=0: #str型だから長さが０でない間ループするに変更
    for i in range(2):
        slist.append(s[i])   
        if "".join(slist)=="dre" or "".join(slist)== "era":
            for i in range(3,7):
                slist.append(s[i])
                
                if "".join(slist)=="dream":
                    for i in range(8,10):
                        slist.append(s[i])
                        if "".join(slist)=="dreamer":
                            s=s[7:] #sの７番以降をsに定義
                            slist=[]
                        else:
                            s=s[5:]
                            slist=[]
                            
                elif "".join(slist)=="erase":
                    for i in range(8,9):
                        slist.append(s[i])
                        if "".join(slist)=="eraser":
                            s=s[6:]
                            slist=[]
                        else:
                            s=s[5:]
                            slist=[]
                
                else:
                    print("NO")
                    exit()
        else:
            print("NO")
            exit()
                    
print ("YES")    

#ABC049C

s=input()
word=["dream","dreamer","erase","eraser"]

r_s=s[::-1]
r_word=[w[::-1]for w in word]

i=0
while i<len(r_s):
    found=False
    for word in r_word: #r_wordsをwordに入れる
        if r_s[i:i+len(word)]==word: #r_s[i~wordの長さまで]とwordが一致するか
            found=True
            i+=len(word)#iを進める
            break
    if not found:
        print("NO")
        exit()

print("YES")

'''   
s=input()
word=["dream","dreamer","erase","eraser"]

r_s=s[::-1]
r_word=[w[::-1]for w in word]

i=0
while i<len(r_s):
    found=False
    for word in r_word:
        if r_s[i:i+len(word)]==word:
            found=True
            i+=len(word)
            break
    if found==False:
        print("NO")
        exit()

print("YES")
        

























