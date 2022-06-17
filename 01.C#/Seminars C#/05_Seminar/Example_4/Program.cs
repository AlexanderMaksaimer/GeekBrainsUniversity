//Задайте одномерный массив из 123 случайных чисел. Найдите количество элементов массива, значения которых лежат в отрезке [10,99]. 

int[] arrayCreation(int length){
    int[] arr = new int[length];
    Random rnd = new Random();
    for ( int i = 0 ; i< length ; i ++){
        arr[i] = rnd.Next(0,150);
    }
return arr;}

string PrintArray(int[] array){
    string result = String.Empty;
    for (int i = 0; i < array.Length; i++){
        if (i == 0) result = "[ "+result + Convert.ToString(array[i]) + ", ";
        else if (i < array.Length-1)
            result = result + Convert.ToString(array[i]) + ", ";
        else result = result + Convert.ToString(array[i]) + "]";
    }
return result;
}

int countLookUp(int[] array,int minLookUp,int maxLookUp){
    int count = 0;
    foreach(int item in array){
        if ((item >= minLookUp) && (item <= maxLookUp)) count++;
    }
return count;
}


Console.Write("Размер массива : ");
int length = int.Parse(Console.ReadLine());
int[] array = arrayCreation(length);

Console.WriteLine($"[10,99] ; {PrintArray(array)} - > {countLookUp(array,10,99)}");