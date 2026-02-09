N = int(input())
arr = list(map(int,input().split()))

arr_list = sorted(arr)

total = 0
time_list = []
for num in arr_list:
    total += num
    time_list.append(total)

print(sum(time_list))