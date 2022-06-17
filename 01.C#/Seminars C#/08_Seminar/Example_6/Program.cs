//Вывести первые N строк треугольника Паскаля. Сделать вывод в виде равнобедренного треугольника


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

string[,] PascalTriangleCreation(int N)
{
    string[,] array = new string[N,N];
    for ( int i = 0 ; i < N ; i ++)
        for ( int j = 0 ; j < N ; j ++)
            if ( (j == 0) || ( j == N-1)) array[i,j] = 1 ;  
}