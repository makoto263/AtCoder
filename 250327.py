#B-Full Hose

'''
A=list(map(int,input().split()))
A.sort()


fullhouse="False"

for i in range(len(A)):
    count_x=A.count(A[i])

    if count_x>=3:
        for j in range(len(A)):
            count_y=A.count(A[j])
            if count_y>=2 and A[i]!=A[j]:
                fullhouse="True"
                print("Yes")
                exit()
   
    elif count_x>=2:
        for j in range(len(A)):
            count_y=A.count(A[j])
            if count_y>=3 and A[i]!=A[j]:
                fullhouse="True"
                print("Yes")
                exit()

print("No")

#Chat GPT
from collections import Counter

A = list(map(int, input().split()))  # 入力をリストに変換
A.sort()  # ソート

count_dict = Counter(A)  # 各要素の出現回数を取得

has_three = None  # 3枚のカードを持つ値
has_two = None  # 2枚のカードを持つ値

for key, count in count_dict.items():
    if count >= 3:
        has_three = key  # 3枚以上のカードを記録
    elif count >= 2:
        has_two = key  # 2枚以上のカードを記録

# 異なる値で 3枚 + 2枚 の組み合わせがあればフルハウス
if has_three is not None and has_two is not None and has_three != has_two:
    print("Yes")
else:
    print("No")

'''
from collections import Counter

N=int(input())
A=list(map(int,input().split()))

count_dict=Counter(A)
has_one=[]

for key, count in count_dict.items():
    if count==1:
        has_one.append(key)

has_one.sort()

if has_one==[]:
    print(-1)
else:
    print(A.index(has_one[-1])+1)


















