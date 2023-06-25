read_list = []
with open("HW1/file.txt", "r") as f: # чтоб не закрывать файл дополнительным кодом
    number_line = 1
    for line in f:
        try:
            s = ' '.join(line.split()) # удаляем перенос из строки (удаляем /n)
            print(f"Номер строки: {number_line} Содердимое: {s}")
            read_list.append(int(s))
        except ValueError:
            print("Некорректное значение числа в файле!")
        number_line +=1

print(read_list) # посмотреть на список чисел
print(f"Сумма чисел в файле равна {sum(read_list)}") # подсчет суммы чисел в файле с выводом