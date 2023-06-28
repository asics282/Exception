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

## Задача3:
Напишите программу, которая запрашивает у пользователя три числа и выполняет следующие проверки:
Если первое число больше 100, выбросить исключение NumberOutOfRangeException с сообщением "Первое число вне допустимого диапазона".
Если второе число меньше 0, выбросить исключение NumberOutOfRangeException с сообщением "Второе число вне допустимого диапазона".
Если сумма первого и второго чисел меньше 10, выбросить исключение NumberSumException с сообщением "Сумма первого и второго чисел слишком мала".
Если третье число равно 0, выбросить исключение DivisionByZeroException с сообщением "Деление на ноль недопустимо".
В противном случае, программа должна выводить сообщение "Проверка пройдена успешно". Необходимо создать 3 класса собвстенных исключений

```python
class NumberOutOfRangeException(Exception):
    pass

class NumberSumException(Exception):
    pass

class DivisionByZeroException(Exception):
    pass

def check_numbers():
    try:
        first_number = int(input("Введите первое число: "))
        second_number = int(input("Введите второе число: "))
        third_number = int(input("Введите третье число: "))

        if first_number > 100:
            raise NumberOutOfRangeException("Первое число вне допустимого диапазона")
        if second_number < 0:
            raise NumberOutOfRangeException("Второе число вне допустимого диапазона")
        if first_number + second_number < 10:
            raise NumberSumException("Сумма первого и второго чисел слишком мала")
        if third_number == 0:
            raise DivisionByZeroException("Деление на ноль недопустимо")

        print("Проверка пройдена успешно")
    except NumberOutOfRangeException as e:
        print("Ошибка: " + str(e))
    except NumberSumException as e:
        print("Ошибка: " + str(e))
    except DivisionByZeroException as e:
        print("Ошибка: " + str(e))
    except ValueError:
        print("Ошибка: Некорректный ввод числа")
check_numbers()
```

---
Подготовил студент Geek Brains - **[Ивлев Павел](https://github.com/asics282)**.