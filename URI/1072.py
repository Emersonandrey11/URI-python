N = int(input())
dost = []
dentro = 0
fora = 0
cm =0

while cm < N:
    vector = int(input())
    dost.append(vector)
    cm = cm + 1

for i in dost:
    if (i >= 10) and (i <= 20):
        dentro = dentro + 1
    if (i < 10) or (i > 20):
        fora = fora + 1

print(dentro, "in")
print(fora, "out")