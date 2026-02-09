n, m = map(int,input().split())
arr = list(map(int,input().split()))
# 입력받기 완료
# m = 0도 될 수 있다는 것!! (범위 사소하지만 잘 챙기기)


window = sum(arr[:m])
max_sum = window

for i in range(m,len(arr)): #시작을 n-m으로 두면 틀린다 (제한적인 예시를 가지고 단정짓지 말자)

    window = window + arr[i] - arr[i-m]
    if window > max_sum:
        max_sum = window

print(max_sum)