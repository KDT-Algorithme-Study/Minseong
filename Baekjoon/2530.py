"""
1번 라인 : 현재 시각  A (0 ≤ A ≤ 23), 분 B (0 ≤ B ≤ 59)와 초 C (0 ≤ C ≤ 59)가 정수
2번 라인 : 필요한 시간 D (0 ≤ D ≤ 500,000)가 초 단위

출력 : 시 분 초  
디지털 시계는 23시 59분 59초에서 1초가 지나면 0시 0분 0초가 된다.
"""

def time_cal(d):
    si = int(d / 3600)
    bun = int((d % 3600) / 60)
    cho = int((d % 3600) % 60)
    return si , bun , cho

a,b,c = map(int , input().split())
d = int(input())
si, bun , cho = time_cal(d)

total_si = si + a
total_bun = bun + b
total_cho = cho + c

# 초를 올림 처리
if total_cho >= 60:
    total_bun += total_cho // 60
    total_cho %= 60

# 분을 올림 처리
if total_bun >= 60:
    total_si += total_bun // 60
    total_bun %= 60

# 시를 올림 처리
if total_si >= 24:
    total_si %= 24

print(total_si,total_bun,total_cho)


