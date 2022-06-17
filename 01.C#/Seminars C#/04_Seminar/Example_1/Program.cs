// 

Console.WriteLine("Введите число:");
string numberStr = Console.ReadLine();
int number = int.Parse(numberStr);
if(IsNumberPositive(number))
{
    int sum = GetSumFromOnetoNumber(number);
    Console.WriteLine($"Сумма числе от 1 до n: {sum}");
}
else
{
    Console.WriteLine("Некорректное число");
}


// проверяет что число положительное
bool IsNumberPositive(int number)
{
    return number > 0;
}

//считает сумму числе от 1 до number
int GetSumFromOnetoNumber(int number)
{
    int sum = 0;
    
    for(int i = 1; i < number; i++)
        sum += i; // sum = sum + i;
    
    return sum;

}