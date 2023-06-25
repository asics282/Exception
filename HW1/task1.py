number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))

try:
    result = number1/number2
    print(result)
except ZeroDivisionError:
    print("Деление на ноль недопустимо")

print('Для завершения работы программы нажмите "Enter"...')
end = input()