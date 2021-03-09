from sys import argv

def salary(production, rate, prize):
    result = (int(production) * int(rate)) + int(prize)
    return result

print(f'зарплата работника равна : {salary(*argv[1:4])}')
