/*Задача 72: Заданы 2 массива: info и data. В массиве info 
хранятся двоичные представления нескольких чисел (без разделителя). 
В массиве data хранится информация о количестве бит, которые занимают 
числа из массива info. Напишите программу, которая составит массив 
десятичных представлений чисел массива data с учётом информации из массива info.

входные данные:
info = {0, 1, 1, 1, 1, 0, 0, 0, 1 }
data = {2, 3, 3, 1 }
выходные данные:
1, 7, 0, 1

*/

int Translate(int[] info)
{
    int result = 0;
    for (var i = 0; i < info.Length; i++)
    {
        result += info[info.Length - i - 1] * ((int)Math.Pow(2, i)); // 1 1 1   1*1 (1)+ 1*2 + 1* 4    0 1 2 3 
    }
    return result;
}

void GetNumber(int[] info, int[] data)
{
    int count = 0;
    foreach (var item in data)
    {
        int[] temp = new int[item];
        int j = 0;
        for (var i = count; i < item + count; i++)
        {
            temp[j++] = info[i];
        }
        Console.Write($"{Translate(temp)}  ");
        count += item;
    }
}


int[] info = { 0, 1, 1, 1, 1, 0, 0, 0, 1 };
int[] data = { 2, 3, 3, 1 };
GetNumber(info, data);
//  1, 7, 0, 1