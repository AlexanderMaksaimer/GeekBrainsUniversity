import java.util.*;

public class Lesson5 {

    public static void main(String[] args) {
        HashMap<Integer, String> hashMap = new HashMap<>();

        hashMap.put(1, "One");
        hashMap.clear();
        hashMap.put(2, "Two");
        hashMap.put(1, "SecondOne");
        hashMap.replace(1, "ThirdOne");

        System.out.println(hashMap.get(1));
        hashMap.putIfAbsent(3, "Third");

        hashMap.forEach((k, v) -> System.out.println(k+","+v));
        hashMap.containsKey(1);
        hashMap.containsValue("4");
        Set<Integer> keys = hashMap.keySet();
        Collection<String> values = hashMap.values();
        hashMap.remove(3);
        hashMap.isEmpty();
        hashMap.getOrDefault(76, "defaultValue");

        for (String str: hashMap.values()) {
            System.out.println(str);
        }

        for (Integer i: hashMap.keySet()) {
            System.out.println(i);
        }

        for (int i = 0; i < keys.size(); i++) {
            System.out.println(hashMap.getOrDefault(keys.toArray()[i], "defaultValue"));
        }

        LinkedHashMap<String, Integer> linkedHashMap = new LinkedHashMap<>();
        TreeMap<Integer, String> treeMap = new TreeMap<>();
        treeMap.put(1, "shhhhh");


    }

}