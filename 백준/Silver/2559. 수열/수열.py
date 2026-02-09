N,K = map(int, input().split())
arr = list(map(int,input().split()))

window = sum(arr[:K])
max_sum = window

for i in range(K,len(arr)):
    window = window + arr[i] - arr[i-K]
    if window > max_sum:
        max_sum = window

print(max_sum)