
valores = []
acm = 0

for i in range(0, 5):
    numbers = int(input())
    valores.append(numbers)

for j in valores:
    a = j % 2
    if a == 0:
        acm = acm + 1

print(acm,"valores pares")