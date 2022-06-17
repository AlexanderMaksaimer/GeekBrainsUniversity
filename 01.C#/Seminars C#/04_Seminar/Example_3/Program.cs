// Задача 28: Напишите программу, которая принимает на вход число N 
//и выдаёт произведение чисел от 1 до N.

// проверяет что число положительное
bool IsNumberPositive(int number)
{
    return number > 0;
}

//считает произведение от 1 до number
int GetSumFromOnetoNumber(int number)
{
    int ProdSqr = 1;
    
    for(int i = 1; i < number; i++)
        ProdSqr += i; // sum = sum + i;
    
    return ProdSqr;

}


Console.WriteLine("Введите число:");
string numberStr = Console.ReadLine();
int number = int.Parse(numberStr);
if(IsNumberPositive(number))
{
    int sum = GetSumFromOnetoNumber(number);
    Console.WriteLine($"Произведение чисел от 1 до n: {sum}");
}
else
{
    Console.WriteLine("Некорректное число");
}
