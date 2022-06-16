//Задача 64: Задайте значения M и N. Напишите программу, которая выведет все натуральные числа в промежутке от M до N.

//M = 1; N = 5. -> "1, 2, 3, 4, 5"
//M = 4; N = 8. -> "4, 6, 7, 8"


int GetDemension(string message)
{
    Console.WriteLine(message);
    int demension = int.Parse(Console.ReadLine());
    return demension;
}

//печатаем массив из натуральных чисел из указанного промежутка (М и N)
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