## 구매한 각 물건의 가격과 개수
## 구매한 물건들의 총 금액

## 1. 1번입력 input을 사용해 총 금액 X를 입력받음
## 2. 2번입력 물건의 종류의 수 N을 받음
## 3. N개에 대한 물건 가격 : a 와 개수 : b

## 출력: 가격과 개수로 계산한 총 금액 == 영수증 금액
## -> yes / no

def multiplication(a,b):
    return a * b
    
c = []
k = 0
x = int(input())
N = int(input())
for i in range(N):
    a, b = map(int,input().split())
    c.append(multiplication(a,b))
    

for j in range(len(c)):
    k += c[j]

if x == k:
    print("Yes")
else:
    print("No")
    
    
    


