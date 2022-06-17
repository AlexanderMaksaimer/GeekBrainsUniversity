/*Задача 42: Напишите программу, которая будет преобразовывать десятичное число в двоичное.
45 -> 101101
3  -> 11
2  -> 10
*/

char [] Converting (int number)
{
    string ostatokOtDelenia = string.Empty;
    while (number >= 1)
    {
    string str;
    int ost = number % 2;
    ostatokOtDelenia += ost.ToString();
    number = number / 2;
    }
    return ostatokOtDelenia.Reverse().ToArray();
}

void PrintArray (char [] sting)
{
    for(int i = 0; i < sting.Length; i++)
    {
        Console.Write(sting[i]);
    }
}

Console.WriteLine("Введите число");
int number = int.Parse(Console.ReadLine());
char [] sting = Converting(number);
PrintArray(sting);