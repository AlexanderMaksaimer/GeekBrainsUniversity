//Задача 36: Задайте одномерный массив, заполненный случайными числами. Найдите сумму элементов, стоящих на нечётных позициях.
//[3, 7, 23, 12] -> 19
//[-4, -6, 89, 6] -> 0

//метод, который инициализирует массив заполненный случайными положительными трёхзначными числами
int [] InitArray(int length)
{
    int [] arr = new int[length];
    Random rnd = new Random();

    for(int i = 0; i < length; i++)
    {
        arr[i] = rnd.Next(-100, 100); // [a,b)
    }

    return arr;
}

// метод, который найдет сумму элементов стоящих на нечетных позициях
int SumInArray (int []array)
{
    int count = 0;
    for(int i = 0; i < array.Length; i++)
    {
        if (i %2 != 0) 
            count+=array[i];
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
Console.WriteLine();
int result = SumInArray(array);

Console.WriteLine($" Сумма элементов, стоящих на нечетных позициях в массиве - > {result}");