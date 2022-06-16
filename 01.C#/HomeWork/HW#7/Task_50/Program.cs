/*Задача 50: Напишите программу, которая на вход принимает позиции элемента в двумерном массиве, 
и возвращает значение этого элемента или же указание, что такого элемента нет.
Например, задан массив:
1 4 7 2
5 9 2 3
8 4 2 4
17 -> такого числа в массиве нет
*/

//ввод данных
int GetDemension(string message)
{
    Console.WriteLine(message);
    int demension = int.Parse(Console.ReadLine());
    return demension;
}
//создание матрицы по заданным размерам
int[,] InitMatrix(int firstDemension, int secondDemension)
{
    int[,] matrix = new int[firstDemension, secondDemension];
    Random rnd = new Random();
    for (int i = 0; i < firstDemension; i++)
    {
        for (int j = 0; j < secondDemension; j++)
            matrix[i, j] = rnd.Next(-50, 100);
    }
    return matrix;
}

//вывод матрицы на консоль
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

//Метод вывода поиска значений индекса исходя из ввода пользователем последовательно номера строки и номера столбца

void CheckIndexInMatrix(int[,] array)
{
    int SearchRow = GetDemension("Выберите строку для поиска числа");
    if (SearchRow > array.GetLength(0)) Console.Write($"\n{SearchRow} - > в матрице меньше строк, чем введенное вами значение");
    else 
    {
        int SearchColumn = GetDemension("Выберите столбец для поиска числа");
        if (SearchRow > array.GetLength(1)) Console.Write($"\n{SearchRow} - > в матрице меньше столбцов, чем введенное вами значение");
        else Console.Write($"\nВ строке № {SearchRow} в столбце № {SearchColumn} находится число {array[SearchRow-1,SearchColumn-1]}");
    }
}
//Ввод размерности матрицы (количество строк и столбцов)
int firstDemension = GetDemension("Введите длину для первого разряда матрицы:");
int secondDemension = GetDemension("Введите длину для второго разряда матрицы:");
//Создание матрицы, заполненной рандомными числами
int[,] resultMatrix = InitMatrix(firstDemension, secondDemension);
//Вывод получившейся матрицы
PrintMatrix(matrix: resultMatrix);
Console.WriteLine();
//Поиск нужного элемента в матрице, посредством ввода строки и столбца 
CheckIndexInMatrix(resultMatrix);
Console.WriteLine();