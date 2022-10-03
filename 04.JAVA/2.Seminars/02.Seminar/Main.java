import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
//import java.util.Arrays;
import java.util.Random;


public class Main {

    public static void main(String[] args) {

        Random random = new Random();
        int rnd = random.nextInt(200)-100;
        int rnd2 = random.nextInt(200)-100;
        System.out.println(rnd);
        System.out.println(rnd2);

       File file = new File("file.txt");
       if (!file.exists()) {
           try {
               file.createNewFile();
               FileWriter fileWriter = new FileWriter(file.getAbsoluteFile());
               fileWriter.append("Hello World!");
               fileWriter.flush();
           } catch (IOException e) {
               throw new RuntimeException(e);
           }
       }

        String str = "New Line New";

        str = str + "!";

        System.out.println(str);

        String tmp = str.toLowerCase();
        str = tmp;
        System.out.println(str);

        if (str.equals("New")) System.out.println("equals");
        if (str.contains("New")) System.out.println("contains");
        tmp = str.replace("new", "Not new");
        str = tmp.replaceFirst("Not new", "cat");
        System.out.println(str);

        String[] aStr = str.split(" ");

        int aRnd = Math.abs(rnd);
        System.out.println(Integer.toBinaryString(aRnd));
        System.out.println(Integer.toBinaryString(aRnd).length());

        String str2 = "";
        long start, end;
        start = System.currentTimeMillis();

        for (int i = 0; i < 100; i++) {
            str2 += Character.getName(i);
        }

        end = System.currentTimeMillis();
        System.out.println(end - start);

        StringBuilder stringBuilder = new StringBuilder("");

        start = System.currentTimeMillis();

        for (int i = 0; i < 100; i++) {
            stringBuilder.append(Character.getName(i));
        }

        end = System.currentTimeMillis();
        System.out.println(end - start);

        if (9 % 2 == 0) System.out.println("Not");

    }
}