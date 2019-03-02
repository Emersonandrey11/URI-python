
num = int(input())
x = 0

last = list(range(1, 1001))

for i in last:
    a = i % 2
    if (a != 0) and (i <= num):
        print(i)




