// 1.Создайте новый список массивов, добавить несколько цветов (строку) и вывести коллекцию на экран.
// 2.Проитерируйте все элементы списка цветов и добавте к каждому символа '!'.
// 3.Напишите программу для вставки элемента в список массивов в первой позиции.
// 4.Извлеките элемент (по указанному индексу) из заданного списка.
// 5.Обновите элемент массива по заданному индексу.
// 6.Напишите программу для удаления третьего элемента из списка массивов.
// 7.Напишите программу для поиска элемента в списке массивов.
// 8.*Напишите программу для сортировки заданного списка массивов.
// 9.*Напишите программу для копирования одного списка массивов в другой.

import java.util.ArrayList;

public class Programm {
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();  //создание списка цветов
        list.add("White");
        list.add("Orange");
        list.add("Red");
        list.add("Black");
        list.add("Green");
        list.add("Purple");
        list.add("Grey");
        list.add("Blue");
        list.add("SieraBlue");
        System.out.println(list); //вывод
        for (int i = 0; i < list.size(); i++) { // добавление ! в конце каждого элемента
            String temp = list.get(i);
            temp += "!";
            list.set(i, temp);
        }
        System.out.println(list);
        list.add(0, "New Element"); // добавление элемента на 1 позицию 
        System.out.println(list);
        System.out.println(list.get(5)); // Извлекаем элемент с указаным индексом
        list.set(4,"Update"); // обновление элемента
        System.out.println(list);
        list.remove(3); // удаление 3 элемента списка
        System.out.println(list);
        System.out.println(list.indexOf("Blue!")); // ищем индекс элемента
        list.sort(null); // сортировка 
        System.out.println(list);
        ArrayList <String> copyList=(ArrayList<String>)list.clone(); // копирование массива
        System.out.println(copyList);
    }

}