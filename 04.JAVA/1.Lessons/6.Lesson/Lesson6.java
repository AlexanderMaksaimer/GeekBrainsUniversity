import java.util.*;

public class Lesson6 {
    public static void main(String[] args) {

        HashMap<Integer, Object> hashMap = new HashMap<>();
        hashMap.put(8673, new Object());
        hashMap.put(8754, new Object());
        hashMap.put(8673, new Object());

        Comparator<Integer> comparator = new Comparator<Integer>() {
            @Override
            public int compare(Integer t0, Integer t1) {
                return new Random().nextInt(3)-1;
            }
        };

        HashSet<Integer> hashSet = new HashSet<>();
        LinkedHashSet<Integer> linkedHashSet = new LinkedHashSet<>();
        TreeSet<Integer> treeSet = new TreeSet<>(comparator);

        for (int i = 0; i < 10; i++) {
            int r = new Random().nextInt(100);
            System.out.println(r);
            hashSet.add(r);
            linkedHashSet.add(r);
            treeSet.add(r);
        }

        System.out.println("----");
        treeSet.forEach(n -> System.out.println(n));

        System.out.println("----");
        hashSet.forEach(n -> System.out.println(n));
        System.out.println("----");
        linkedHashSet.forEach(n -> System.out.println(n));
        treeSet.forEach(n -> System.out.println(n));
        System.out.println("----");

        SortedSet<Integer> hs = treeSet.headSet(50);
        SortedSet<Integer> ts = treeSet.tailSet(50);
        int c = treeSet.ceiling(50);
        int f = treeSet.floor(50);
        treeSet.higher(50);
        treeSet.lower(50);

        treeSet.forEach(n -> System.out.println(n));

        ArrayList<Integer> list = new ArrayList<>();
        Iterator<Integer> it = treeSet.iterator();
        while (it.hasNext()){
            int i = it.next();
            if (it.hasNext()) {
                list.add(i + it.next());
            } else list.add(i);
        }
    }
}
