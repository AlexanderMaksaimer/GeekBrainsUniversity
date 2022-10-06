// Написать программу позволяющую ввести разнотипные данные пользователей, такие как ФИО, возраст, пол итд. Хранение данных организовать в списках. 
// После ввода программа сортирует пользователей по возрасту и выводит отсортированный список на экран.

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Scanner;


public class Programm4 {
    public static void main(String[] args) {
        String encoding = System.getProperty("console.encoding", "utf-8");
        Scanner scan = new Scanner(System.in, encoding);
        ArrayList<String> name = new ArrayList<>();
        ArrayList<Integer> age = new ArrayList<>();
        LinkedList<Integer> id = new LinkedList<>();
        boolean run = true;

        int count = 0;
        while (run) {
            System.out.println("Введите имя человека: ");
            name.add(scan.nextLine());
            System.out.println("Введите возраст человека: ");
            age.add(scan.nextInt());
            id.add(count);
            count++;
            System.out.println("Продолжаем?");
            System.out.println("Введите: нет, если закончили ввод. Для продолжения введите любой другой символ");
            scan.nextLine();
            if (scan.nextLine().toLowerCase().equals("нет")) {
                run = false;
            }
        }

        for (int index = 0; index < id.size(); index++) {
            System.out.print(name.get(id.get(index)) + ", ");
            System.out.print(age.get(id.get(index)) + ", ");
            System.out.println(id.get(index) + " ");
        }
        // Сортируем получившиеся данные
        int sort = id.size() - 1;
        while (sort > -1) {
            int ageMax = age.get(id.get(sort));
            int index = sort;

            for (int i = 0; i < sort; i++) {
                if (ageMax > age.get(id.get(i))) {
                    index = i;
                    ageMax = age.get(id.get(i));
                }
            }
            int temp = id.get(index);
            id.set(index, id.get(sort));
            id.remove(sort);
            id.add(temp);
            sort--;
        }

        System.out.println("Проведена сортировка по возрасту:");
        for (int index = 0; index < id.size(); index++) {
            System.out.print(name.get(id.get(index)) + ", ");
            System.out.print(age.get(id.get(index)) + ", ");
            System.out.println(id.get(index) + " ");
        }
    }
}
