N, X = map(int,input().split())
arr = list(map(int, input().split()))


window = sum(arr[:X])
max_val = window
sum_list = [window]

for i in range(X,len(arr)):
    window = window + arr[i] - arr[i-X]
    sum_list.append(window)
    if window > max_val:
        max_val = window

if max_val == 0:
    print('SAD')

else:
    print(max_val)
    print(sum_list.count(max_val))