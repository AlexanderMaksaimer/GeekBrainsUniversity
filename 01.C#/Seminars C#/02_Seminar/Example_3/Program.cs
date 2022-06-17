// Напишите программу, которая будет принимать на вход два числа и выводить, является ли второе число кратным первому
//34, 5 ->  Не кратно, остаток 4
//16, 4 -> кратно

Console.WriteLine("Введите первое число: ");
string firstNumberStr = Console.ReadLine();
Console.WriteLine("Введите второе число: ");
string secondNumberStr = Console.ReadLine();
int first = int.Parse(firstNumberStr);
int second = int.Parse(secondNumberStr);

int result = first % second;

if(result == 0)
    Console.WriteLine ("кратно");
else
    Console.WriteLine ($"некратно, остаток {result}");