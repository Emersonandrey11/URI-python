num1 = int(input())
num2 = int(input())
soma = 0

if num1 == num2:
    print(0)

if num1 > num2:
    numbers2 = list(range(num2, num1+1))
    for i in numbers2:
        a = i % 2
        if (a !=0) and (i > num2) and (i < num1):
            soma = soma + i
    print(soma)

