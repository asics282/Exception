try:
    old = int(input('Введите ваш вазраст: '))
    print(f"Ваш возраст {old}")
except ValueError:
    print("Некорректный ввод")

print('Для завершения работы программы нажмите "Enter"...')
end = input()