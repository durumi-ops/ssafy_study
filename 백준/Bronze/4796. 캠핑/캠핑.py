data = []

while True:
    L,P,V = map(int,input().split())
    if L==0 and P==0 and V==0:
        break
    data.append([L,P,V])

for i in range(len(data)):
    days = 0
    days += data[i][0] * (data[i][2]//data[i][1])
    # days += data[i][2] % data[i][1] #무조건 작은 숫자 더하면 안됨
    days += min(data[i][0],data[i][2] % data[i][1])
    print(f'Case {i+1}: {days}')