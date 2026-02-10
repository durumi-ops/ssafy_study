N = int(input())

#시작: N
#종료: 1
#누적: N~1

def fct(N):
    if N <= 0:
        return 1
    return N * fct(N-1)

result = fct(N)
print(result)