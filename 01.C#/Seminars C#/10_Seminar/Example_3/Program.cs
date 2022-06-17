/*Задача 70: Напишите программу, которая на вход принимает два числа 
и выдаёт первые N чисел, для которых каждое следующее равно сумме двух предыдущих. 
3 и 4, N = 5 -> 3 4 7 11 18
6 и 10, N = 4 -> 6 10 16 26 
*/

int GetNumber(string message)
{
    System.Console.Write(message);
    while (true)
    {
        if (int.TryParse(Console.ReadLine(), out int result))
            return result;
        else
            System.Console.WriteLine("ошибка");
    }
}

void Progressiv(int first, int second, int count)
{
    int i = 0;
    if (i < count)
    {
        Console.Write($"{first} ");
        Progressiv(second, first + second, count - 1);
    }
    else
        return;
}

int firstNumber = GetNumber("Введите первое число = ");
int secondNumber = GetNumber("Введите второе число = ");
int countNumber = GetNumber("Введите второе число = ");
Progressiv(firstNumber, secondNumber, countNumber);