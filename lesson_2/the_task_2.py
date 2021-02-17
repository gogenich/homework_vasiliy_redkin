l = input('введете значения списка через пробел: ')
l = l.split()
print(l)
i = 0
for x in l[1:: 2]:
    l[i + 1], l[i] = l[i], l[i+1]
    i = i + 2
print(l)
