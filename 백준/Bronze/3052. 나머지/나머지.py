#10번 입력받는다
arr = []
for _ in range(10):
    arr.append(int(input()))

# 42로 나눈 나머지를 담을 리스트를 생성한다.
li = []

# arr에 있는 숫자를 차례대로 42로 나누며 나머지에 대해 li 리스트에 넣는다. (중복허용하면서)
for i in range(len(arr)):
    li.append(arr[i]%42)

# 중복을 제거한 set를 생성한다.
ans = set(li)

# 총 개수를 출력한다.
print(len(ans))