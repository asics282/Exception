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