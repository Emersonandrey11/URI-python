
numbers = []
neg = 0
posi = 0
impar = 0
par = 0

for i in range(0,5):
    enter = int(input())
    numbers.append(enter)

for j in numbers:
    a = j % 2
    if j > 0:
        posi = posi + 1

    if j < 0:
        neg = neg + 1

    if a == 0:
        par = par + 1

    if a != 0:
        impar = impar + 1

print(par,"valor(es) par(es)")
print(impar,"valor(es) impar(es)")
print(posi,"valor(es) positivo(s)")
print(neg,"valor(es) negativo(s)")
