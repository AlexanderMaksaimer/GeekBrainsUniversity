// Напишите программу, которая по заданному номеру четверти показывает диапазон возможных точек в этой плоскости
// сначала получить число - > проверить 1/2/3/4 -> выдать диапазон четверти
int GetQuarter()
{
    while (true)
    {
        Console.WriteLine("Введите номер четверти, диапазон которой хотите узнать");
        int quater = Convert.ToInt32(Console.ReadLine());
        if (quater != 1 && quater != 2 && quater != 3 && quater != 4)
        {
            Console.WriteLine("Введите число от 1 до 4");
        }
        else
            return quater;
    }
}

void GetRange(int quater) // функция принимает выходной параметр
{
    if(quater ==1)
    {
        Console.WriteLine("х > 0, y > 0");
    }
    else if (quater == 2)
    {
        Console.WriteLine ("x < 0, y > 0");
    }
    else if (quater == 3)
    {
        Console.WriteLine ("x < 0, y < 0");
    }
    else
    {
        Console.WriteLine (" x > 0, y < 0");
    }
}

int giveQuater = GetQuarter();
GetRange(giveQuater);