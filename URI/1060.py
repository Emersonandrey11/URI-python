acm = 0

list = []

for j in range(0, 6):
    numbers = float((input()))
    list.append(numbers)

for i in list:
    if (i) > 0:
        acm = acm + 1
print(acm,"valores positivos")
