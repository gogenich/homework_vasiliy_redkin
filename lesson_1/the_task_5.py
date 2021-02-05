proceeds = int(input('введите выручку предприятия: '))
costs = int(input('введите издержки предприятия: '))
if proceeds > costs:
    print('мы работаем в прибыль')
    profit = proceeds - costs
    profitability = (profit / proceeds) * 100
    print(f'прибыль предприятия = {profit}, а рентабельность = {int(profitability)}% ')
    staff = int(input('введите колличество сотрудников: '))
    profit_staff = profit / staff
    print(f'прибыль на кажного сотрудника составила: {profit_staff} монет')
elif proceeds == costs:
    print('мы работем в 0')
else:
    print('мы работаем в убыток')