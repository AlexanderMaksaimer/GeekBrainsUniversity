int[] array = { 1, 25, 38, 4, 55, 46, 87, 78, 18, 18, 59 };

int n = array.Length;
int find = 18;

int index = 0;

while (index < n)
{
    if(array[index] == find)
    {
        Console.WriteLine(index);
        break;
    }
    //index = index +1;
    index++; 
}
