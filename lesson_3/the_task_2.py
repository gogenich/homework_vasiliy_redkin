def my_fanc (name, surname, year_of_birth, City_of_residence, email, telfon):
    print(f'имя: {name}; фамилия: {surname}; год рождения: {year_of_birth}; город проживания: {City_of_residence}; emeil: {email}; телефон: {telfon}.')

name = input('введите Ваше имя: ')
surname = input('введите Вашу фамилию: ')
year_of_birth = input('введите Ваш год рождения: ')
City_of_residence = input('введите Ваш город проживания: ')
email = input('введите Ваш emeil: ')
telfon = input('введите Ваш телефон: ')

my_fanc(name, surname, year_of_birth, City_of_residence, email, telfon)