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