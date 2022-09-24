//Задание к семинару № 1:

// 1. Выбросить случайное целое число в диапазоне от -1000 до 1000 и сохранить в i
// 2. Посчитать и сохранить в n номер старшего значащего бита выпавшего числа
// 3. Найти все кратные n числа в диапазоне от i до Short.MAX_VALUE сохранить в массив m1
// 4. Найти все некратные n числа в диапазоне от Short.MIN_VALUE до i и сохранить в массив m2
// 5. Сохранить оба массива в файлы с именами m1 и m2 соответственно.
// Пункты реализовать в методе main
// *Пункты реализовать в разных методах

import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.concurrent.ThreadLocalRandom;

public class Main {

    static int getRandom() {
        int randomNum = ThreadLocalRandom.current().nextInt(-1000, 1000 + 1);
        return randomNum;
    }

    static int getHierBitNum(int inputNum) {
        int res = 0;
        while (inputNum != 0) {
            inputNum >>= 1;
            res++;
        }
        return res;
    }

    static Integer[] getArrayMax(int multNum, int num) {
        ArrayList<Integer> tempArray = new ArrayList<>();
        for (int i = num; i <= Short.MAX_VALUE; i++) {
            if (i % multNum == 0) {
                tempArray.add(i);
            }
        }
        Integer[] array = new Integer[tempArray.size()];
        tempArray.toArray(array);
        return array;
    }

    static Integer[] getArrayMin(int multNum, int num) {
        ArrayList<Integer> tempArray = new ArrayList<>();
        for (int i = num; i >= Short.MIN_VALUE; i--) {
            if (i % multNum != 0) {
                tempArray.add(i);
            }
        }
        Integer[] array = new Integer[tempArray.size()];
        tempArray.toArray(array);
        return array;
    }

    static void printArray(Integer[] array) {
        System.out.print("{");
        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i]);
            if (i < array.length - 1) {
                System.out.print(", ");
            }
        }
        System.out.print("}");
    }

    static void addInFile(Integer[] array, String name) {
        try (FileWriter fw = new FileWriter(name + ".txt", false)) {
            fw.write("{");
            for (int i = 0; i < array.length; i++) {
                fw.append(array[i].toString());
                if (i < array.length - 1) {
                    fw.append(", ");
                }
            }
            fw.write("}");
        } catch (IOException ex) {
            System.out.println(ex.getMessage());
        }
    }

    public static void main(String[] args) {

        int i = getRandom();
        int n = getHierBitNum(i);
        Integer[] file1 = getArrayMax(n, i);
        Integer[] file2 = getArrayMin(n, i);

        System.out.println(i);
        System.out.println(n);
        addInFile(file1,"m1");
        addInFile(file2, "m2");

    }
}