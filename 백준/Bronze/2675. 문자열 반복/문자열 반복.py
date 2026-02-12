T= int(input())

p=[]
for i in range(T):
    ans = []
    num, chr = input().split()
    chr_list = list(chr)
    for i in range(len(chr_list)):
        ans.append(chr_list[i]*int(num))
    p.append(''.join(ans))

for i in range(len(p)):
    print(p[i])