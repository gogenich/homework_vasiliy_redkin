def factorial (namb):
    rezult = 1
    i = 1
    while i <= namb:
        rezult = rezult * i
        yield rezult
        i = i + 1

namb = int(input('введите число: '))
for el in factorial(namb):
    print(el)
