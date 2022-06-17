// Напишите программу, которая принимает на вход число и выдает количество цифр в числе

string GetNumber ()
{
    return Console.ReadLine();
}

int CountNum(string str)
{
    int num = int.Parse(str);
    int count = 0;
    //int? count;

    while (num > 0)
    {
        num = num / 10;
        count++;
    }
    return count;
}

//int CountNum(string str)
//{
//    return str.Length;
//}

Console.WriteLine("Введите число: ");
int countNum = CountNum(GetNumber());

Console.WriteLine(countNum);
