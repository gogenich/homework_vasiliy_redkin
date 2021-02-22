
def my_func(a: int, b: int) -> float:
    ''' фукция с a/b '''
    try:
        rezult = a/b
        return rezult
    except ZeroDivisionError as err:
        print(f'функция задала переменной b значение 0, ошибка: {err}')

print(my_func(1, 0))