## Задача 1:
Напишите программу, которая запрашивает у пользователя число и проверяет, является ли оно положительным. Если число отрицательное или равно нулю, программа должна выбрасывать исключение InvalidNumberException с сообщением "Некорректное число". В противном случае, программа должна выводить сообщение "Число корректно".

```python
class MyError(Exception): # класс Исключения
    def __init__(self, text):
        self.txt = text

def Main():
    print("Начало работы")
    while True:
        number = input('Введите положительное число: ')
        try:
            number = int(number)
            if number <= 0:
                raise MyError("Некорректное число") # принудительный вызов исключения
        except MyError as mr: # присваивание исключения переменной
            print(mr)
        except ValueError: # отлов некорректного ввода
            print("Некорректный ввод")
        else:
            print("Число корректно")

        print('Для завершения работы программы нажмите "Enter", или введите любой символ для продолжения...')
        end = input()
        if not end:
            break
    print('Завершение работы')

Main()
```

## Задача 2:
Напишите программу, которая запрашивает у пользователя два числа и выполняет их деление. Если второе число равно нулю, программа должна выбрасывать исключение DivisionByZeroException с сообщением "Деление на ноль недопустимо". В противном случае, программа должна выводить результат деления

```python
class MyError(Exception): # класс Исключения
    def __init__(self, text):
        self.txt = text

def Main():
    print("Начало работы")
    while True:
        number1 = input("Введите первое число: ")
        number2 = input("Введите второе число: ")

        try:
            number1 = int(number1)
            number2 = int(number2)
            if number2 == 0:
                raise MyError("Некорректное число") # принудительный вызов исключения
        except MyError as mr: # присваивание исключения переменной
            print(mr)
        except ValueError:
            print('Некорректный ввод')
        else:
            result = number1/number2
            print(f'{number1}/{number2} = {result}')

        print('Для завершения работы программы нажмите "Enter", или введите любой символ для продолжения...')
        end = input()
        if not end:
            break
    print('Завершение работы')

Main()
```

---
Подготовил студент Geek Brains - **[Ивлев Павел](https://github.com/asics282)**.