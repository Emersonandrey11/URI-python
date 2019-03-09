N = int(input())

num = list(range(1, 2001))

for i in num:
    if i % 2 == 0 and i <= N:
        a = pow(i, 2)
        print("%d^2" %i, "=", a)
