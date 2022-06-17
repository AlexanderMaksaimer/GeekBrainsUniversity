//Задача 44: Не используя рекурсию, выведите первые N чисел Фибоначчи. Первые два числа Фибоначчи: 0 и 1.

List<int> Fibonaci(int n)
{
    List<int> fib = new List<int>();
    fib.Add(0);
    fib.Add(1);
    for ( int i = 2 ; i < n ; i++)
        fib.Add(fib[i-1]+fib[i-2]);
return fib;        
}

void FibArray(int n)
{
    Console.Write(" 0 1 ");
    int sum1 = 0;
    int sum2 = 1;
    int temp;
    for ( int i = 2 ; i < n ; i++)
    {
        temp = sum1+sum2;
        Console.Write($"{temp} ");
        sum1 = sum2;
        sum2 = temp;
    }
        
}

void printList(List<int> list)
{
    for ( int i = 0 ; i< list.Count ; i++ )
        Console.WriteLine($"{i+1} = {list[i]}");
}

void printListLine(List<int> list)
{
    for ( int i = 0 ; i< list.Count ; i++ )
        Console.Write($"{list[i]} ");
}

Console.Write("Введите N * больше или равно 2: ");
int n = int.Parse(Console.ReadLine());
Console.Write($"N = {n} - > ");
printListLine(Fibonaci(n));
Console.Write("\n\n");

printList(Fibonaci(n));
Console.Write("\n\n");
FibArray(n);