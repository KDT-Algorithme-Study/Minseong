
"""
5 (1 2 3 4 5)
3 1 4 3 2

1 = 3 
2 = 3 + 1 
3 = 3 + 1 + 4
4 = 3 + 1 + 4 + 3
5 = 3 + 1 + 4 + 3 + 2
시간 => 39분

-> 1 2 3 4 5 수가 채워지고 
-> 두번째 줄에서 입력받는 순서에 따라 첫번째에서 입력했던 사람들의 순서가 결정되어야함



"""

N = int(input())
P = list(map(int,input().split()))

people = []
result = []
for i in range (N):
    people.append(i+1)

P.sort()

total_time = 0
current_time = 0

for i in range(len(P)):
    current_time += P[i]
    total_time += current_time

print(total_time)