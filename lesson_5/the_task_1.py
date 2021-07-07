from io import TextIOWrapper
fail = open('the_task_1.txt', 'w', encoding = 'UTF-8' )
while True:
    fail.writelines(input('введите давнные в фаил the_task_1.txt: ')+'\n')
    marker = input('продолжать ввод данных да/нет: ')
    if marker == 'нет':
        break
fail.close()
print('end')