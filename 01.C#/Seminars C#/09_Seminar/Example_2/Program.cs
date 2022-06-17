//Задача 65: Задайте значения M и N. Напишите программу, которая выведет все натуральные числа в промежутке от M до N.

int NumberInput(string text)//Метод ввода и проверки на число
{
    bool isInputInt = true;
    int number =0;
    while (isInputInt)
    {
        Console.Write($"Введите {text} :");
        string numberSTR = Console.ReadLine();
        if (int.TryParse(numberSTR, out int numberInt))
        {
            if (numberInt <= 0) Console.WriteLine("Введите число больше нуля");
            else
            {
                number = numberInt;
                isInputInt = false;
            } 
        }
        else 
            Console.WriteLine("Ввели не число");
    }
    return number;
}

void PrintNumbers(int numberN,int numberM)
{
    if (numberN != numberM)
    {
        PrintNumbers(numberN-1,numberM);
        Console.Write($" {numberN} ");
    }
    else  Console.Write($"{numberN}");
}

int numberN = NumberInput("число N ");
int numberM = NumberInput("число M ");

PrintNumbers(numberN,numberM);