nome1 = input()
nome2 = input()
nome3 = input()

if nome1 == "vertebrado":
    if nome2 == "ave":
        if nome3 == "carnivoro":
            print("aguia")
        else:
            print("pomba")
    else:
        if nome3 == "onivoro":
            print("homem")
        else:
            print("vaca")
else:
    if nome2 == "inseto":
        if nome3 == "hematofago":
            print("pulga")
        else:
            print("lagarta")
    else:
        if nome3 == "onivoro":
            print("minhoca")
        else:
            print("sanguessuga")
