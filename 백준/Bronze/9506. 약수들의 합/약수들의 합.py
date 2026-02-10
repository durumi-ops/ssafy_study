import sys
sys.setrecursionlimit(10**6)

#시작: 1
#종료: N//2
#num: 1씩 증가하는 숫자, acc_list: 약수 리스트
#누적값: 약수(리스트로)

def recur(num,acc_list):
    #약수 체크 로직
    if num > N //2:
        return acc_list

    if N%num == 0:
        acc_list.append(num)

    return recur(num + 1, acc_list)



while True:
    N = int(input())
    if N == -1:
        break

    divisors = recur(1,[])

    if sum(divisors) == N:
        print(f'{N} = {" + ".join(map(str,divisors))}')
    else:
        print(f'{N} is NOT perfect.')