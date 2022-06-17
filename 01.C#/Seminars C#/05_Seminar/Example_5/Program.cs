//Найдите произведение пар чисел в одномерном массиве. Парой считаем первый и последний элемент, второй и предпоследний и т.д. Результат запишите в новом массиве.

//Найдите произведение пар чисел в одномерном массиве. Парой считаем первый и последний элемент, второй  
// и предпоследний и т.д. Результат запишите в новом массиве. 
//[1 2 3 4 5] -> 5 8 3 
//[6 7 3 6] -> 36 21 
 
int[] ArrayCreation(int length){ 
    int[] arr = new int[length]; 
    Random rnd = new Random(); 
    for ( int i = 0 ; i< length ; i ++){ 
        arr[i] = rnd.Next(1,6); 
    } 
return arr;} 
 
void PrintArray(int[] array){ 
    string result = String.Empty; 
    for (int i = 0; i < array.Length; i++){ 
        if (i == 0) result = "[ " + Convert.ToString(array[i]) + ", ";//string builder 
        else if (i < array.Length-1) 
            result = result + Convert.ToString(array[i]) + ", "; 
        else result = result + Convert.ToString(array[i]) + "]"; 
    } 
Console.WriteLine(result); 
} 
int [] Multiple (int[] array) 
{ 
    int length = 0; 
    bool even =false; 
    if (array.Length % 2 == 0) 
    { 
        length = array.Length / 2; 
        even = true; 
    } 
    
    else  
    length = array.Length / 2 + 1; 
    int[] newArray = new int[length]; 
    for (int i = 0; i < array.Length/2;i++) 
    { 
        newArray[i] = array[i] * array[array.Length -1 - i]; 
         
    } 
    if (even == false) 
    { 
        newArray[newArray.Length -1] = array[array.Length/2]; 
         
    } 
 
    return newArray; 
 
 
} 
int [] arr = ArrayCreation(4); 
PrintArray(arr); 
int [] result = Multiple(arr); 
PrintArray(result);