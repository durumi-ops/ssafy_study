T = int(input())
for i in range(T):
    list = []
    S,R = input().split()  # 숫자와 문자를 string으로 입력받는다
    num = int(S)
    for ch in R:
        list.append(ch*num)
    print(''.join(list))