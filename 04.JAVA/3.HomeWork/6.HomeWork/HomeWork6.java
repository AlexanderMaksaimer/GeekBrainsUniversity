// 1. Объявить и инициализировать множества HashSet hs, LinkedHashSet lhs и TreeSet ts
// 2. Добавить в множества по 10 случайных целочисленных ключей.
// 3. Пройти по множеству hs и, при условии наличия соответствующего ключа в множестве lhs, удалить ключ из hs
// 4. Пройти по множеству lhs и, при условии отсутствия соответствующего ключа в множестве ts, добавит ключ в ts
// 5. Объявить и инициализировать множество TreeSet ts1 с компаратором Integer (-1 при значении %2==0 ;0 при ==;1 при значении %2!=0). 
// Заполнить ts1 15 случайными числами и вывести на печать.
// 6.*Объявить и инициализировать множество TreeMap tm с компаратором Integer (-1 при значении %2==0 ;0 при ==;1 при значении %2!=0). 
// Заполнить tm 15 случайными числами и вывести на печать.
import java.util.LinkedHashSet;
import java.util.Random;
import java.util.TreeSet;
import java.util.Comparator;
import java.util.HashSet;

public class HomeWork6 {
    public static void main(String[] args) { // 1. Объявить и инициализировать множества HashSet hs, LinkedHashSet lhs и TreeSet ts
        HashSet<Integer> hs = new HashSet<>();
        LinkedHashSet<Integer> lhs = new LinkedHashSet<>();
        TreeSet<Integer> ts = new TreeSet<>();

        // 2. Добавить в множества по 10 случайных целочисленных ключей.
        while (hs.size() != 10) {
            for (int i = 0; i < 10; i++) {
                hs.add(new Random().nextInt(10));
                lhs.add(new Random().nextInt(10));
                ts.add(new Random().nextInt(10));
            }
        }

       // 3. Пройти по множеству hs и, при условии наличия соответствующего ключа в множестве lhs, удалить ключ из hs
        System.out.println("До манипуляций");
        System.out.println(hs);
        System.out.println(lhs);
        System.out.println("-----");
        System.out.println("После манипуляций");
        hs.removeAll(lhs);
        System.out.println(hs);

        // 4. Пройти по множеству lhs и, при условии отсутствия соответствующего ключа в множестве ts, добавит ключ в ts
        lhs.addAll(ts);

        // 5. Объявить и инициализировать множество TreeSet ts1 с компаратором Integer (-1 при значении %2==0 ;0 при ==;1 при значении %2!=0). 
        // Заполнить ts1 15 случайными числами и вывести на печать.
        TreeSet<Integer> ts1 = new TreeSet<>(new Comparator<Integer>() {
            @Override
            public int compare(Integer int1, Integer int2) {
                return int1 == int2 ? 0 : int2 % 2 == 0 ? -1 : 1;}
        });

        for (int i = 0; i < 15; i++) {
            ts1.add(new Random().nextInt(100));
        }
        System.out.println(ts1);
    }
}