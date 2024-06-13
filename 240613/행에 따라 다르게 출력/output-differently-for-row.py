n = int(input())
for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            print(j+1+(2*n+1)*int(i/2), end = ' ')
        else:
            print(n+2+2*j+(n+1)*(i-1), end = ' ')
    print()