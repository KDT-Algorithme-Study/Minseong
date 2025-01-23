"""
1. 첫 줄에 S , R1을 입력
-> S = R1 + R2 / 2 
2S = R1+R2
R2 = 2S - R1

"""

r1 , s = map(int, input().split())
r2 = 2*s - r1
print(r2)

