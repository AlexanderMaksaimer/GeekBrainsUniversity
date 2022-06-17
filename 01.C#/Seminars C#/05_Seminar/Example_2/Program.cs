// Напишите программу замены элементов массива: положительные элементы замените на отрицательные и наоборот
//[-4,-8,8,2] -> [4,8,-8,-2]

//метод, который инициализирует массив из 12 элементов в промежутке от [-9, 9]
int [] InitArray(int length) //значимый тип
{
    int [] arr = new int[length];
    Random rnd = new Random();

    for(int i = 0; i < length; i++)
    {
        arr[i] = rnd.Next(-9, 10); // [a,b)
    }

    return arr;
}

//метод, в котором мы заменяем отрицательное значение на положительное

int [] MultipleNegative (int [] array) //ссылочный тип
{
    int [] newArray = new int [array.Length];
    for(int i = 0; i < array.Length; i++)
    {
        newArray [i] = array[i] * -1;
    }
    return newArray;
}

//метод, который печатает наш массив на консоль
void PrintArray(int [] arr)
    {
    foreach(int item in arr)
        Console.Write($"{item} ");
    }


Console.WriteLine("Введите размерность массива:");
int length = int.Parse(Console.ReadLine());
int[] arr = InitArray(length);
Console.WriteLine("Массив: ");
PrintArray(arr);
Console.WriteLine();

int[] array = MultipleNegative(arr);

Console.WriteLine("Полученный массив: ");

PrintArray(array);