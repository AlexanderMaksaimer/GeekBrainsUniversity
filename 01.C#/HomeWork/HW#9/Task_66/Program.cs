//Задача 66: Задайте значения M и N. Напишите программу, которая найдёт сумму натуральных элементов в промежутке от M до N.
//M = 1; N = 15 -> 120
//M = 4; N = 8. -> 30


int GetDemension(string message)
{
    Console.WriteLine(message);
    int demension = int.Parse(Console.ReadLine());
    return demension;
}
//метод поиска суммы
int SummFromMtoN(int numberM, int numberN)
{
    if ( numberN != numberM ) numberN = SummFromMtoN(numberM,numberN-1)+numberN;
    return  numberN;
}
//печатаем полученный перечень чисел
void PrintArrayFromMtoN(int m, int n, int k) 
{
    if ( n == m ) Console.Write($"'{m}, ");
    else 
    {
        PrintArrayFromMtoN(m,n-1,k);
        if (k == n) Console.Write($"{n}'");
        else Console.Write($"{n}, ");
    }
}


int m = GetDemension("Введите число M: ");
int n = GetDemension("Введите число N: ");
Console.WriteLine();
Console.Write($"Выводим натуральные числа в промежутке от M ({m}) до N ({n}) -> ");
PrintArrayFromMtoN(m,n,n);
Console.WriteLine();
int sum = SummFromMtoN(m,n);
Console.WriteLine($"\nСумма натуральных чисел от M ({m}) до N ({n}) -> {sum}");