// Задача 38: Задайте массив вещественных чисел. Найдите разницу между максимальным и минимальным элементов массива.
//[3 7 22 2 78] -> 76

//метод, который инициализирует массив заполненный случайными вещественными числами
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

// метод поиска минимального и максимального значения в массиве
(int,int) maxAndMin(int[] array)
{ 
    int min = array[0];
    int max = array[0];
    for (int i = 0; i < array.Length; i++)
    {
        if (array[i] < min)
            min = array[i];
        if (array[i] > max)
            max = array[i];
    }
return (min,max);
}

//метод, который печатает массив на консоль
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

int min =0;
int max = 0;

(min,max) = maxAndMin(array);

Console.WriteLine($"Минимальное значение массива - > {min}");
Console.WriteLine($"Максимальное значение массива -> {max}");
Console.WriteLine($"Разница между максимальным и минимальным значением массива равняется {max-min}");
