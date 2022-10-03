// Напишите программу на Java, чтобы найти наименьшее окно в строке, содержащей все символы другой строки.
// Напишите программу на Java, чтобы проверить, являются ли две данные строки вращением друг друга.
// *Напишите программу на Java, чтобы перевернуть строку с помощью рекурсии.
// Дано два числа, например 3 и 56, необходимо составить следующие строки: 3 + 56 = 59 3 – 56 = -53 3 * 56 = 168 Используем метод StringBuilder.append().
// Замените символ “=” на слово “равно”. Используйте методы StringBuilder.insert(),StringBuilder.deleteCharAt().
// *Замените символ “=” на слово “равно”. Используйте методы StringBuilder.replace().
// **Сравнить время выполнения пункта 6 со строкой содержащей 10000 символов "=" средствами String и StringBuilder.

import java.util.Scanner;

public class Program {
    static String CheckValue(Scanner lookUp) {
        String str = lookUp.nextLine();
        return str;
    }

    static void SearchWindow(String str1, String str2) { // поиск окна в строке
        if (str1.contains(str2))
            System.out.println("Окно найдено!");
        else
            System.out.println("Окошек не найдено");
    }

    static boolean Rotation(String s1, String s2) { // вращение строк
        return (s1.length() == s2.length()) && ((s1 + s1).indexOf(s2) != -1);
    }
 
    static String Reverse(String str) { // рекурсия (разворот)
        if (str.length() <= 1) {
            return str;
        }
        return Reverse(str.substring(1)) + str.charAt(0);
    }

    static StringBuilder getLine() { // сравнить время выполнения замены = на равно 
        StringBuilder str = new StringBuilder();
        for (int i = 0; i < 10000; i++) {
            str.append("=");
        }
        return str;
    }

    static long getTime(String str) {
        long start, end;
        for (int i = 0; i < 10001; i++) {
            str += "=";
        }
        start = System.currentTimeMillis();

        str.replace("=", "равно");

        end = System.currentTimeMillis();

        return end - start;
    }

    

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
            System.out.println("Введите текст для проверки");
        String str = CheckValue(input);
            System.out.println("Введите одно словечко");
        String str2 = CheckValue(input);
        
        SearchWindow(str, str2);
        if (Rotation(str, str2))
        System.out.println("Являются вращением");
        else
        System.out.println("Не являются вращением");
        System.out.println(Reverse(str));
        String nums1 = "3";
        String nums2 = "56";
        StringBuilder res = new StringBuilder(); // составить строчки
        res.append(nums1 + "+" + nums2 + "=" + "59" + " " + nums1 + "-" + nums2 + "="
        + "-59" + " " + nums1 + "*"
        + nums2 + "=" + "168");
        System.out.println(res);

        res.insert(res.indexOf("="), "Равно");
        res.deleteCharAt(res.indexOf("="));
        System.out.println(res);
        res.replace(res.indexOf("="), res.indexOf("=") + 1, "Равно");
        res.replace(res.indexOf("="), res.indexOf("=") + 1, "Равно");
        System.out.println(res);

        String timeTest = "";
        
        System.out.println(getTime(timeTest));
        
    }
}