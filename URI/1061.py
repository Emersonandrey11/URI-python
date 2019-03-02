list1 = []
list2 = []

day1 = int(input("Dia: "))

for i in range(0, 3):
    numbers = int(input())
    list1.append(numbers)

day2 = int(input("Dia: "))

for i in range(0, 3):
    numbers1 = int(input())
    list2.append(numbers1)


a3 = 60 - list1[2]
a2 = 60 - list1[1]
a1 = 24 - list1[0]

a77 = a1 + list2[0]
a78 = a2 + list2[1]
a79 = a3 + list2[2]

end_line = day2 - 1
count = end_line - day1

if a79 >= 59:
    a78 = a78 + 1
    a79 = (a79 - 60)

if a78 >= 59:
    a77 = a77 + 1
    a78 = (a78 - 60)

if a77 >= 23:
    count = count + 1
    a77 = (a77 - 24)

real_time = [a77, a78, a79]

print(count, "dia(s)")
print(a77, "hora(s)")
print(a78, "minuto(s)")
print(a79, "segundo(s)")
#print(end_line)
#print(real_time)
#print(a1)
#print(a2)
#print(a3)
