
DDD = [61, 71, 11, 21, 32, 19, 27, 31]
city = ["Brasilia", "Salvador", "Sao Paulo", "Rio de Janeiro", "Juiz de Fora", "Campinas", "Vitoria", "Belo Horizonte"]

enter = int(input())
b = DDD.count(enter)

if b == 0:
    print("DDD nao cadastrado")
else:
    a = DDD.index(enter)
    print(city[a])






