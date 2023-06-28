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