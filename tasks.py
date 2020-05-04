'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
string = '000000000'
i = 1
while i<=5:
    print(i, string)
    i+=1
'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
i = 0
n = 0
while i<10:
    number = int(input("Введите цифру: "))
    i+=1
    if number == 5:
        n+=1
print(n)
'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
sum = 0
for i in range(1,101):
    sum+=i
print(sum)
'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
multiply = 1
for i in range(1,11):
    multiply*=i
print(multiply)
'''
Задача 5
Вывести цифры числа на каждой строчке.
'''
number = int(input('Введите ваше число: '))
while number>0:
    figure = number % 10
    number = number // 10
    print(figure)
'''
Задача 6
Найти сумму цифр числа.
'''
number = int(input("Введите ваше число: "))
sum = 0
while number > 0:
    figure = number % 10
    number = number // 10
    sum = sum + figure
print(sum)


'''
Задача 7
Найти произведение цифр числа.
'''
number = int(input('Введите ваше число: '))
multiplication = 1
while number > 0:
    figure = number % 10
    number = number // 10
    multiplication = multiplication * figure
print(multiplication)

'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
integer_number = int(input('Введите ваше число: '))
while integer_number > 0:
    if integer_number%10 == 5:
        print('Yes')
        break
    integer_number = integer_number//10
else: print('No')

'''
Задача 9
Найти максимальную цифру в числе
'''
number = int(input('Введите ваше число: '))
max_number = number % 10
while number > 0:
    number = number // 10
    figure = number % 10
    if max_number < figure:
        max_number = figure
print(max_number)

'''
Задача 10
Найти количество цифр 5 в числе
'''
number = int(input('введите ваше число: '))
i = 0
while number > 0:
    figure = number % 10
    number = number // 10
    if figure == 5:
        i = i + 1
print(i)