acm = 0
media = []
list = []
a = 0

for j in range(0, 6):
    numbers = float((input()))
    list.append(numbers)

for i in list:
    if (i) > 0:
        acm = acm + 1
        media.append(i)

for j in media:
    a = a + j

print(acm,"valores positivos")
media2 = a/len(media)
print("%.1f" % media2)

