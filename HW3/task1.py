# Определение класса пользовательского исключения
class InvalidInputException(Exception):
    pass

# Определение класса
class PowerCalculator:
    # Метод для вычисления степени
    def calculatePower(self, base, exponent):
        if base == 0 and exponent < 0:
            # Вызов пользовательского исключения InvalidInputException
            raise InvalidInputException("Неверный ввод: основание не может быть равно нулю, а показатель степени не может быть отрицательным.")
        return base ** exponent

# Основная функция программы
def main():
    # Создание объекта класса PowerCalculator
    calculator = PowerCalculator()
    print("Начало работы")
    while True:
        try:
            base = int(input("Введите первое число (основание): "))
            exponent = int(input("Введите второе число (степень): "))
            result = calculator.calculatePower(base, exponent) # Вычисление степени с помощью метода calculatePower
            print("Результат:", result)
        except ValueError: # Обработка исключения при неверном вводе чисел
            print("Неверный ввод: введите допустимые числа.")
        except InvalidInputException as error: # Обработка пользовательского исключения InvalidInputException
            print(error)
        
        print('Для завершения работы программы нажмите "Enter", или введите любой символ для продолжения...')
        end = input()
        if not end:
            break    
    print('Завершение работы')

main()