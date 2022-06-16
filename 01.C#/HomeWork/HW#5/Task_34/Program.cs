//Задача 34: Задайте массив заполненный случайными положительными трёхзначными числами. 
//Напишите программу, которая покажет количество чётных чисел в массиве.
//[345, 897, 568, 234] -> 2

//метод, который инициализирует массив заполненный случайными положительными трёхзначными числами
int [] InitArray(int length)
{
    int [] arr = new int[length];
    Random rnd = new Random();

    for(int i = 0; i < length; i++)
    {
        arr[i] = rnd.Next(100, 1000); // [a,b)
    }

    return arr;
}

//метод, который посчитает количество четных чисел в массиве
int CheckArray (int []array)
{
    int count = 0;
    foreach(int item in array)
    {
        if (item %2==0) count++;
    }
return count;
}

////метод, который печатает массив на консоль
void PrintArray(int [] arr)
    {
    foreach(int item in arr)
        Console.Write($"{item} ");
    }

Console.Write("Размер массива : ");
int length = int.Parse(Console.ReadLine());
int [] array = InitArray(length);
Console.WriteLine("Полученный массив:");
PrintArray(array);
int result = CheckArray(array);

Console.WriteLine($" Количество четных чисел в массиве - > {result}");