N = int(input())
dt = list(map(int,input().split()))
pr = list(map(int,input().split()))

min_p = pr[0]

total = pr[0]*dt[0]

for i in range(1, N-1):
    if pr[i] < min_p:
        min_p = pr[i]
        total += min_p * dt[i] #dt 초기값 정으 필요 ***********

    else:
        total += min_p*dt[i]

print(total)