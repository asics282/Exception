## Простая задача 1: Проверка деления на ноль
Напишите программу, которая запрашивает у пользователя два целых числа и выполняет их деление. Если второе число равно нулю, выбросите исключение ArithmeticException с сообщением "Деление на ноль недопустимо". Иначе выведите результат деления на экран.

### [Решение на Python](task1.py)
```python
number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))

try:
    result = number1/number2
    print(result)
except ZeroDivisionError:
    print("Деление на ноль недопустимо")

print('Для завершения работы программы нажмите "Enter"...')
end = input()
```

### [Решение на Java](task1.java)
```java
package HW1;
import java.util.Scanner;

public class task1 {
    public static void main(String[] args) {
        System.out.println("Введите первое число: ");
        Scanner scan = new Scanner(System.in);
        int number1 = scan.nextInt();
        System.out.println("Введите второе число: ");
        int number2 = scan.nextInt();

        try {
            int result = number1/number2;
            System.out.println(result);
        } catch (Exception ArithmeticException) {
            System.out.println("Деление на ноль недопустимо");
        }
    }
}
```
### Простая задача 2: Обработка некорректного ввода
Напишите программу, которая запрашивает у пользователя его возраст. Если введенное значение не является числом, выбросите исключение NumberFormatException с сообщением "Некорректный ввод". Иначе выведите возраст на экран.

### [Решение на Python](task2.py)
```python
try:
    old = int(input('Введите ваш вазраст: '))
    print(f"Ваш возраст {old}")
except ValueError:
    print("Некорректный ввод")

print('Для завершения работы программы нажмите "Enter"...')
end = input()
```
### [Решение на Java](task2.java)
```java
package HW1;
import java.util.Scanner;

public class task2 {
    public static void main(String[] args) {
        System.out.println("Введите первое число: ");
        Scanner scan = new Scanner(System.in);
        String input = scan.nextLine();
        try {
            int old = Integer.parseInt(input);
            System.out.println("Ваш возраст " + old);
        } catch (NumberFormatException e) {
            System.out.println("Некорректный ввод");
        }
    }
}
```

### Сложная задача: Чтение файла и подсчет суммы чисел (решена на Python)
Напишите программу, которая считывает содержимое текстового файла, в котором каждая строка содержит одно число. Программа должна подсчитать сумму всех чисел в файле. Если встретится строка, которая не может быть преобразована в число, выбросите исключение NumberFormatException с сообщением "Некорректное значение числа в файле".

### [Решение на Python](task3.py)
```python
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
```

---
Подготовил студент Geek Brains - **[Ивлев Павел](https://github.com/asics282)**.