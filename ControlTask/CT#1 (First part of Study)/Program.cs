/*Написать программу, которая из имеющегося массива строк формирует массив из строк, 
длина которых меньше либо равна 3 символа. Первоначальный массив можно ввести с клавиатуры, либо задать на старте выполнения алгоритма. 
При решении не рекомендуется пользоваться коллекциями, лучше обойтись исключительно массивами.

Примеры:

["hello", "2", "world", ":-)"] -> ["2", ":-)"]

["1234", "1567", "-2", "computer sience"] -> ["-2"]

["Russia","Denmark", "Kazan"] ->[]*/

// 1. метод создания массива строк
// 2. метод создания нового массива с определенной длиной (например, как в условии <=3 символа)
// 3. вывод первого и второго массива на консоль

string[] FirstArray()//Метод создания массива 
{
    
    int index = 0;
    string text = String.Empty;
    List<string> arrayList = new List<string>();
    do
    {
        Console.Write($"Эллемент массива № {index} : ");
        text = Console.ReadLine();
        if (text == null) text = String.Empty;// проверка пустых значений
        arrayList.Add(text);
        index++;
        Console.WriteLine("\tДля продолжения ввода элементов нажмите любую кнопку, для выхода нажмите ESC");
    }
    while (Console.ReadKey().Key != ConsoleKey.Escape);

    string[] array = new string[arrayList.Count];

    for (int i = 0; i < array.Length; i++) array[i] = arrayList[i];

    return array;
}

(int, string[]) SecondArray(string[] array)//Метод создания нового массива
{
    int count = 0;
        for (int i = 0; i < array.Length; i++) if (array[i].Length <= 3) count++;
            
    string[] arrayResul = new string[count];
    return (count, arrayResul);
}

void FillArray(string[] array, string[] fillArray)//Метод заполнения массива 
{
    int index = 0;
        for (int i = 0; i < array.Length; i++) if (array[i].Length <= 3)
            {
                fillArray[index] = array[i];
                index++;
           }
            
}

string PrintArray(string[] array) // Метод печати массива
{
    string result = String.Empty;
    result += "[";
    for (int i = 0; i < array.Length; i++)
    {
        result += '"' + array[i] + '"';
        if (i < array.Length - 1) result += ',';
    }
    result += "]";
    return result;
}


Console.WriteLine("Введите с клавиатуры эллементы массива ");
string[] array = FirstArray(); // Создаю изначальный массив
(int count, string[] secondArray) = SecondArray(array); // Создаю второй массив
FillArray(array, secondArray); // Заполняю второй массив в соответствии с условием (вывод тех элементов, чья длина <=3 символов)
Console.WriteLine();
Console.WriteLine("Первоначальный массив:");
Console.WriteLine($"\n{PrintArray(array)} "); //Вывод на консоль изначального массива
Console.WriteLine("Результат задачи (массив из элементов, длина которых <=3):");
Console.WriteLine($"\n{PrintArray(secondArray)}"); //Вывод на консоль результата (массив длинной <=3 символа)
