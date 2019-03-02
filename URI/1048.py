
salary = float(input())

if salary > 0 and salary <= 400:
    reajust = salary*(0.15)
    new_salary = salary + reajust
    percentual = "Em percentual: 15 %"
    print("Novo salario: %.2f" %new_salary)
    print("Reajuste ganho: %.2f" %reajust)
    print(percentual)

elif salary > 400 and salary <= 800:
    reajust = salary*(0.12)
    new_salary = salary + reajust
    percentual = "Em percentual: 12 %"
    print("Novo salario: %.2f" %new_salary)
    print("Reajuste ganho: %.2f" %reajust)
    print(percentual)

elif salary > 800 and salary <= 1200:
    reajust = salary*(0.10)
    new_salary = salary + reajust
    percentual = "Em percentual: 10 %"
    print("Novo salario: %.2f" %new_salary)
    print("Reajuste ganho: %.2f" %reajust)
    print(percentual)

elif salary > 1200 and salary <= 2000:
    reajust = salary*(0.07)
    new_salary = salary + reajust
    percentual = "Em percentual: 7 %"
    print("Novo salario: %.2f" %new_salary)
    print("Reajuste ganho: %.2f" %reajust)
    print(percentual)

else:
    reajust = salary*(0.04)
    new_salary = salary + reajust
    percentual = "Em percentual: 4 %"
    print("Novo salario: %.2f" %new_salary)
    print("Reajuste ganho: %.2f" %reajust)
    print(percentual)