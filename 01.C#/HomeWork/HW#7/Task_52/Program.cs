/*Задача 52: Задайте двумерный массив из целых чисел. Найдите среднее арифметическое элементов в каждом столбце.
Например, задан массив:
1 4 7 2
5 9 2 3
8 4 2 4
Среднее арифметическое каждого столбца: 4,6; 5,6; 3,6; 3.
*/


int GetDemension(string message)
{
    Console.WriteLine(message);
    int demension = int.Parse(Console.ReadLine());
    return demension;
}

//Инициализация заполнения матрицы рандомными числами
int[,] InitMatrix(int firstDemension, int secondDemension)
{
    int[,] matrix = new int[firstDemension, secondDemension];
    Random rnd = new Random();
    for (int i = 0; i < firstDemension; i++)
    {
        for (int j = 0; j < secondDemension; j++)
            matrix[i, j] = rnd.Next(1, 100);
    }
    return matrix;
}

//Вывод заполненной матрицы
void PrintMatrix(int[,] matrix)
{
    Console.WriteLine("Заполненная матрица");
    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        for (int j = 0; j < matrix.GetLength(1); j++)
            Console.Write($"{matrix[i, j]} ");
        Console.WriteLine();
    }
}

//Метод определения среднего арифмитического каждого СТОЛБЦА!

void CheckColumnMatrix(int[,] matr)
{
    for (int i = 0; i < matr.GetLength(0); i++)
    {
        int summ = 0;
        for (int j = 0; j < matr.GetLength(1); j++)
        {
            summ = summ + matr[j, i];
        }
        double average = summ / matr.GetLength(0);
        int n = i + 1;
        Console.WriteLine($"Среднее арифмитическое для столбца № " + n + " равняется " + (double)average/matr.GetLength(0));
    }

}


//Ввод количества строк и столбцов для матрицы и инициализация ее создания
int firstDemension = GetDemension("Введите длину для первого разряда матрицы:");
int secondDemension = GetDemension("Введите длину для второго разряда матрицы:");
int [,] result = InitMatrix(firstDemension, secondDemension);

//Вывод получившейся матрицы
PrintMatrix(matrix: result);
Console.WriteLine();
//Вывод результата расчетов среднего арифмитического для каждого столбца в матрице
CheckColumnMatrix(result);