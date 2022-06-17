//Задача 69: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

System.Console.OutputEncoding = System.Text.Encoding.Unicode;
Console.Clear();

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

int Stepeni(int numberA, int numberB)
{
    if ( numberB != 1 ) 
        numberA = Stepeni(numberA,numberB-1)*numberA;
    return numberA;
}

int numberA = NumberInput("числоА");
int numberB = NumberInput("числоВ");

int stepeni = Stepeni(numberA,numberB);

Console.WriteLine($"{numberA} в степени {numberB} = {stepeni}");