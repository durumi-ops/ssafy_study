N,K = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]

y_list = []
x_list = []

for i in range(len(arr)):
    y_list.append(arr[i][1])

for i in range(len(arr)):
    x_list.append(arr[i][0])

ice_list = [0]*(max(y_list)+1)

for i in range(len(arr)):
    ice_list[y_list[i]] = x_list[i]

window = sum(ice_list[:K*2+1]) # window = sum(ice_list[:7]) 오답: 7은 내 예시에서 케이스..!!!
max_sum = window

for i in range(K*2+1,len(ice_list)):
    window = window + ice_list[i] - ice_list[i-1-K*2]

    if window > max_sum:
        max_sum = window

print(max_sum)