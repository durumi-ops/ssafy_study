cal = input()
cal_list = cal.split('-')
first_sum = sum(map(int, cal_list[0].split('+')))
ans = first_sum
for i in range(1,len(cal_list)): # for i in range(cal_list[1:]으로 쓰면 틀린다!!)
    ans -= sum(map(int, cal_list[i].split('+')))

print(ans)