// //Задача 39: Напишите программу, которая перевернёт одномерный массив (последний элемент будет на первом месте, а первый - на последнем и т.д.)

int[] GetArray(int length)
{
    Random rnd = new Random();
    int[] array = new int[length];
    for (int i = 0 ; i < length ; i ++)
        array[i] = rnd.Next(0,15);
return array;
}

void PrintArray(int[] array)
{
    foreach(int num in array)
        Console.Write($"{num} ");
}
// перевернет и создаст новый массив
int[] ReverceArray(int[] array)
{
    //array.Reverse(); - хитропопый вариант =)
    int[] arrayNew = new int[array.Length];
    for (int i = 0 ; i < array.Length ; i ++)
        arrayNew[i] = array[array.Length - 1 - i];
return arrayNew;
}

// массив перевернет сам себя
void ReverseArraySelf(int[]array)
{
    array.Reverse();
}

Console.Write("Введие размер массива : ");
int length = int.Parse(Console.ReadLine());

int[] array = GetArray(length);
PrintArray(array);
Console.WriteLine();
PrintArray(ReverceArray(array));