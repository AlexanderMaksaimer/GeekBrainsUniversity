// Написать программу позволяющую ввести разнотипные данные пользователей, такие как ФИО, возраст, пол итд. Хранение данных организовать в списках. 
// После ввода программа сортирует пользователей по возрасту и выводит отсортированный список на экран.

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Scanner;


public class Programm {
    public static void main(String[] args) {
        String encoding = System.getProperty("console.encoding", "utf-8");
        Scanner scan = new Scanner(System.in, encoding);
        ArrayList<Integer> age = new ArrayList<>();
        LinkedList<Integer> id = new LinkedList<>();
        ArrayList<String> name = new ArrayList<>();
        // int numm = scanner.nextInt();
        // String str = scanner.nextLine();
        boolean run = true;

        int count = 0;
        while (run) {
            System.out.println("Введите имя: ");
            name.add(scan.nextLine());

            System.out.println("Введите возраст: ");
            age.add(scan.nextInt());
            id.add(count);
            count++;
            System.out.println("Хотим ли мы продолжить??");
            scan.nextLine();
            if (scan.nextLine().toLowerCase().equals("n")) {
                run = false;
            }
        }

        for (int index = 0; index < id.size(); index++) {
            System.out.print(name.get(id.get(index)) + ", ");
            System.out.print(age.get(id.get(index)) + ", ");
            System.out.println(id.get(index) + " ");
        }
        // Сортируем
        int cnt = id.size() - 1;
        while (cnt > -1) {
            int maxAge = age.get(id.get(cnt));
            int index = cnt;

            for (int i = 0; i < cnt; i++) {
                if (maxAge > age.get(id.get(i))) {
                    index = i;
                    maxAge = age.get(id.get(i));
                }
            }
            int temp = id.get(index);
            id.set(index, id.get(cnt));
            id.remove(cnt);
            id.add(temp);
            cnt--;
        }

        System.out.println("Проведена сортировка:");
        for (int index = 0; index < id.size(); index++) {
            System.out.print(name.get(id.get(index)) + ", ");
            System.out.print(age.get(id.get(index)) + ", ");
            System.out.println(id.get(index) + " ");
        }
    }
}
