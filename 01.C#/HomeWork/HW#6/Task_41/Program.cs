//Задача 41: Пользователь вводит с клавиатуры M чисел. Посчитайте, сколько чисел больше 0 ввёл пользователь.
//0, 7, 8, -2, -2 -> 2
//-1, -7, 567, 89, 223-> 3

//1. Описываем метод для ввода числа и проверяем что ввели именно число
//2. Описываем метод создания массива и вывода положительных значений
//3. Печать на консоль полученного полного массива 
//4. Результат (количество положительных чисел введенных пользоваетелем/ Или информирование об отсутствии положительных чисел среди введенных пользователем)


//1.Описываем метод для ввода числа и проверяем что ввели именно число

int InputNumber(string messageText)  
{
    bool InputIntStr = true;
    int num =0;
    while (InputIntStr)
    {
        Console.Write($"{messageText} число :");
        string numString = Console.ReadLine();
        if (int.TryParse(numString, out int numInt))
        {
            num = numInt;
            InputIntStr = false;
        }
        else 
            Console.WriteLine("Вы ввели не числовое значение ");
    }
    return num;
}

//2.Метод создания массива и вывод положительных значений

(int[] , int) CreateArray(int length)
{
    int[] array = new int[length];
    int countPlus = 0;
    for (int k = 0 ; k < length ; k ++)
    {
        array[k] = InputNumber(messageText: $"{k+1}");
        if (array[k] > 0)
            countPlus++;
    }    
    return (array,countPlus);
}

void PrintArray(int[] array)
{
    foreach(int num in array)
        Console.Write($"{num} ");
}

//Вводим количество чисел, а затем их значения
int numCheck = InputNumber("Введите"); 
Console.WriteLine();

//Создаём массив чисел и показываем количество положительных чисел в нем
(int[] arrayNum , int plusCountNumInArray) = CreateArray(numCheck);
Console.WriteLine();

//Результат вычислений
PrintArray(arrayNum);
Console.WriteLine();
Console.WriteLine($"Количество положительных чисел в заданном массиве: {plusCountNumInArray}");