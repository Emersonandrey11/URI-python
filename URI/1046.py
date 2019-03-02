
hora_inicial = int(input())
hora_final = int(input())
day = 24

if hora_inicial > hora_final:
    duration = ((day - hora_inicial) + hora_final)
    print("O JOGO DUROU", duration, "HORA(S)")

else:
    duration = hora_final - hora_inicial
    print("O JOGO DUROU", duration, "HORA(S)")
