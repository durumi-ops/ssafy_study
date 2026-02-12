T = int(input())

for tc in range(1,T+1):
    cnt = [0] * 10
    max_value = 0
    idx = 0
    N = int(input())   # N은 카드의 숫자
    num = input()       # num은 공백없이 입력받는 숫자
    for n in num:
        cnt[int(n)] += 1


    for i in range(10):
        if cnt[i] >= max_value:
            max_value = cnt[i]
            idx = i

    print(f'#{tc} {idx} {max_value}')