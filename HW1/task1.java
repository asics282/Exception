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