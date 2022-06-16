// Напишите программу, которая на выход
// принимает число и выдает его квадрат (число
//умноженное на само себя)

Console.Write("Введите целое число -> ");
int num = int.Parse (Console.ReadLine());
int numResult = num * num;
Console.Write("Квадрат числа равен -> ");
Console.WriteLine (numResult);
Console.ReadKey ();