n = int(input())

cnt_1 = 1
cnt_2 = n+2

for i in range(n):
    if (i != 0) and (i != 1):
       cnt_1 += 2*n
       cnt_2 += n+2

    for j in range(n):
        if i % 2 == 0:
            print(cnt_1, end = ' ')
            cnt_1 += 1
        else:
            print(cnt_2, end = ' ')
            cnt_2 += 2
    print()