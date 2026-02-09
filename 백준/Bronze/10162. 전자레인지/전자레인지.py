T = int(input())
A, B, C = 0, 0, 0

if T%10 != 0:
    print('-1')
else:
    if T >= 300:
        A += T//300
        if T%300 >=60:
            B += (T%300) // 60
            C += ((T%300)%60)//10
        else:
            C += (T%300)//10

    elif 60<=T<300:
        B += T//60
        C += (T%60)//10

    else:
        C += T//10

    print(A,B,C)