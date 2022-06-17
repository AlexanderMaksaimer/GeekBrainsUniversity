//Задача 71: В некотором машинном алфавите имеются четыре буквы «а», «и», «с» и «в». Покажите все слова, состоящие из n букв, которые можно построить из букв этого алфавита.

System.Console.OutputEncoding = System.Text.Encoding.Unicode;
Console.Clear();

int[] Numbers(int[] bitecodes, int[] bite)
{
    int[] array = new int[bite.Length];
    int index = -1;
    for (int i = 0 ; i < bite.Length ; i ++)
    {
        index += bite[i];
        for ( int j = index; j >= index-(bite[i]-1) ; j--)
        {   
            Console.WriteLine($"{j} - {bitecodes[j]}");
            array[i] += bitecodes[j]*2;
            if ( j == index )
                if ( bitecodes[j] != 0)
                {
                    array[i] += 1;
                }             
        }
    }
    return array;           
}
int[] bytes = {2,3,2,2};
int[] bytescodes = {0,1,1,1,1,0,0,0,1};
int[] array = Numbers(bytescodes,bytes);

for (int i = 0 ; i < array.Length ; i++)
    Console.Write($"{array[i]} ");