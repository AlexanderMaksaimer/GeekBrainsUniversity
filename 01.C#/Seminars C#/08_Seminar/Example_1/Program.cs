﻿//Задача 53: Задайте двумерный массив. Напишите программу, которая поменяет местами первую и последнюю строку массива.

int[,] RandomArrayCreation(int rows , int colums , int minRandom , int maxRandom)//вставил на всякий случай возможность изменения рандомности чисел
{
    Random rnd = new Random();
    int[,] array = new int[rows,colums];
    for ( int i = 0 ; i < rows ; i ++)
        for ( int j = 0 ; j < colums ; j ++)
            array[i,j] = rnd.Next(minRandom,maxRandom+1);
return array;
}

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

void ArrayPrint(int[,] array)
{
    Console.Write("\n");
    for ( int i = 0 ; i < array.GetLength(0) ; i ++)
    {
        Console.Write($"Строка {i+1}");
        for ( int j = 0 ; j < array.GetLength(1) ; j ++)
            Console.Write($"\t{array[i,j],3}"); 
        Console.Write("\n");
    }
}

int[,] LaneChangeInArray(int[,] array)
{
    
    int lastLane = array.GetLength(0)-1;
    int colums = array.GetLength(1);
    int[,] arrayNew = array;
    int temp = 0;
    for ( int i = 0 ; i < colums ; i++)
    {
        temp = arrayNew[0,i];
        arrayNew[0,i] = arrayNew[lastLane,i];
        arrayNew[lastLane,i] = temp;
    }
return arrayNew;
}

int rows = NumberInput("кол-во строк");
int colums = NumberInput("кол-во столбцов");

int[,] array= RandomArrayCreation( rows:rows,
                                    colums:colums,
                                    minRandom:0,
                                    maxRandom:9);
Console.Write("\n Изначальный массив:");
ArrayPrint(array);
int[,] arrayNew = LaneChangeInArray(array);
Console.Write("\n Новый массив:");
ArrayPrint(arrayNew);