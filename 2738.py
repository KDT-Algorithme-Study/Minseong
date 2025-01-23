"""
N * M => A , B
A + B 행렬 덧셈
A : 1 1 1 2 2 2 0 1 0 
B : 3 3 3 4 4 4 5 5 100
"""
# 행렬 크기 입력
N, M = map(int, input().split())

matrix1 = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix1.append(row)

matrix2 = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix2.append(row)

result = []
for i in range(N):
    row = []
    for j in range(M):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)

for row in result:
    print(len(row))
    print(*row)




