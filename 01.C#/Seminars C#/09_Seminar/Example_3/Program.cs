//Задача 67: Напишите программу, которая принимает на вход число и выдаёт сумму цифр в числе.
int numberInput(){//Метод ввода и проверки на число
    bool readlineFromStrToInt = true;
    int number =0;
    while (readlineFromStrToInt){
        Console.Write("Введите число > 10 : ");
        string numberSTR = Console.ReadLine();
        if (int.TryParse(numberSTR, out int numberInt) ){//проверка на число
            number = numberInt;
            if (number < -9 ){
                Console.WriteLine($"Взял число {number} по модулю - > {-number}");
                number *= -1;
                readlineFromStrToInt = false;}
            else if (number <= 9) Console.WriteLine("Ввели число <9");
            else readlineFromStrToInt = false;} } 
return number;}

int symbolSumm(int number){//Модуль суммы цифр в числе через символы
    int sum =0;
    foreach(char num in Convert.ToString(number)) sum = sum +int.Parse(Convert.ToString(num));
return sum;
}

int numberSum(int number){//Модуль математический
    int ost =0;
    int sum =0;
    while ( number > 9){
        ost = number%10;
        number = number/10;
        sum = sum+ost;}
    sum = sum + number;
return sum;}

System.Console.OutputEncoding = System.Text.Encoding.Unicode;

Console.Clear();
Console.WriteLine("Задача 28:\n"+
"\tНапишите программу, которая принимает на вход число \n"+
"\tи выдаёт сумму цифр в числе..\n"+
"\tПример: 9012 -> 12 -- *нажмите Enter для продолжения");
Console.ReadLine();

do{
Console.Clear();

int number = numberInput();

Console.WriteLine($"{number} -> {symbolSumm(number)} - метод через символы");
Console.WriteLine($"{number} -> {numberSum(number)} - математический метод");

Console.WriteLine("Для выходна, нажмите ESCAPE, люба другая кнопка запустить программу повторно.");
} while (Console.ReadKey().Key != ConsoleKey.Escape);