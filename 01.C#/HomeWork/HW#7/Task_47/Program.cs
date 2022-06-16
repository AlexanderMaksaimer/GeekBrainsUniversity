/*Задача 47: Задайте двумерный массив размером m×n, заполненный случайными вещественными числами.
m = 3, n = 4.
0,5 7 -2 -0,2
1 -3,3 8 -9,9
8 7,8 -7,1 9
*/

//метод для ввода количества строк / столбцов 
int GetDemension(string message)
{
    Console.WriteLine(message);
    int demension = int.Parse(Console.ReadLine());
    return demension;
}

//Инициализируем создание матрицы по заданному пользователем количеству строк и столбцов и заполняем рандоными вещественными числами
double[,] InitMatrix(int firstDemension, int secondDemension)
{
    double[,] matrix = new double[firstDemension, secondDemension];
    Random rnd = new Random();
    for (int i = 0; i < firstDemension; i++)
    {
        for (int j = 0; j < secondDemension; j++)
            matrix[i, j] = rnd.NextDouble()*10;
    }
    return matrix;
}

//Метод вывода на консоль заполненной матрицы (с двумя знаками после запятой)
void PrintMatrix(double[,] matrix)
{
    Console.WriteLine("Матрица, заполненная вещественными числами: ");
    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        for (int j = 0; j < matrix.GetLength(1); j++)
            Console.Write($"{(double)matrix[i, j]:N2} ");
        Console.WriteLine();
    }
}

//Ввод количества строк и столбцов для создания матрицы
int firstDemension = GetDemension("Введите длину для первого разряда матрицы:");
int secondDemension = GetDemension("Введите длину для второго разряда матрицы:");
double[,] resultMatrix = InitMatrix(firstDemension, secondDemension);
//Выводим на консоль результат (заполненная вещественными числами матрица)
PrintMatrix(resultMatrix);