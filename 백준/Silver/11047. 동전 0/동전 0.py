N, K = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))
# 입력받기 완료

arr.sort(reverse=True)
count = 0
for i in range(len(arr)):
    if arr[i] > K:
        continue
    else:
        q = K//arr[i]
        count += q
        K = K - (arr[i]*q)

print(count)