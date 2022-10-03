import java.util.*;

public class Lesson3 {
    public static void main(String[] args) {

        ArrayList<Integer> list = new ArrayList<>();
        list.add(2);
        list.add(3);
        list.add(4);
        list.add(5);
        list.add(2, 321);
        list.remove(2);
        list.isEmpty();
        list.set(2, 321);
        list.clear();

        ArrayList<Integer> list1 = new ArrayList<>();
        list1.add(2);
        list.retainAll(list1);
        list.removeAll(list1);

        List list2 = Arrays.asList(1,2,3,5,6,9,4,7,3,6);
        list2.set(2, 5);
        list2.add(2, 5); //РЅРµ РїРѕРґРґРµСЂР¶РёРІР°СЋС‚СЃСЏ!
        list2.remove( list2.size()-1); //РЅРµ РїРѕРґРґРµСЂР¶РёРІР°СЋС‚СЃСЏ!

        for (int i = 0; i < list.size(); i++) {
            System.out.println(list.get(i));
        }

        for (Integer i: list) {
            System.out.println(i);
        }

        ListIterator<Integer> it = list.listIterator();
        while (it.hasNext()){
            Integer i = it.next();
            System.out.println(i);
            it.remove();
        }

        list.forEach(n -> System.out.println(n));

        System.out.println(list);


        LinkedList<Integer> linkedList = new LinkedList<>();


        long start, end;
        start = System.currentTimeMillis();
        for (int i = 0; i < 100000; i++) {
            list.add(0,0);
        }
        System.out.println(System.currentTimeMillis()-start);

        start = System.currentTimeMillis();
        for (int i = 0; i < 100000; i++) {
            linkedList.add(0,0);
        }
        System.out.println(System.currentTimeMillis()-start);




    }
}

