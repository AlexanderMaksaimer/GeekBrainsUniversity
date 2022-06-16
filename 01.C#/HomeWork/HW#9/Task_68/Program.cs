//Задача 68: Напишите программу вычисления функции Аккермана с помощью рекурсии. Даны два неотрицательных числа m и n. 
//m = 2, n = 3 -> A(m,n) = 29

//метод ввода числа и проверки что ввели положительное число
int GetNumber(string text)
{
    bool ThisInt = true;
    int number =0;
    while (ThisInt)
    {
        Console.Write($"Введите {text} :");
        string numberSTR = Console.ReadLine();
        if (int.TryParse(numberSTR, out int intNum))
        {
            if (intNum < 0) Console.WriteLine("Введите положительное число");
            else
            {
                number = intNum;
                ThisInt = false;
            }
            
        }
        else 
            Console.WriteLine("Вы ввели не число");
    }
    return number;
}
//работает правда только с минимальными вводными числами, включая тест кейс (2,3)
long Akkerman(long n, long m)
{
    if (n == 0) return m + 1;
    if (n != 0 && m == 0) return Akkerman(n - 1, 1);
    if (n > 0 && m > 0) return Akkerman(n - 1, Akkerman(n, m - 1));
    return Akkerman(n,m);
}


int m = GetNumber("число m");
int n = GetNumber("число n");
long result = Akkerman(n,m);
Console.WriteLine($" m({m}), n ({n}) -> A({m},{n}) = {result}");