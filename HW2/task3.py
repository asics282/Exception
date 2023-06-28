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