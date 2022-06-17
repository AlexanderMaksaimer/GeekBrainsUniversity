/* Напишите программу, которая принимает на вход три числа и проверяет, может ли существовать треугольник с сторонами такой длины */

/* Теорема о неравенстве треугольника: каждая сторона треугольника меньше суммы двух других сторон*/


int GetNumber(string message)
{
    Console.WriteLine(message);
    int str = int.Parse(System.Console.ReadLine());
    return str;
}

bool TestLine(int lineA, int lineB, int lineC)
{
    bool a1 = lineA < (lineB + lineC);
    bool b1 = lineB < (lineA + lineC);
    bool c1 = lineC < (lineB + lineA);
    return a1 && b1 && c1;    
}


System.Console.Write("Про треугольник");
int lineA = GetNumber("Введите длинну первой стороны = ");
int lineB = GetNumber("Введите длинну второй стороны = ");
int lineC = GetNumber("Введите длинну третьей стороны = ");

bool test = TestLine(lineA, lineB, lineC);
if (test)
{
    Console.WriteLine("Треугольник существует");
}
else
{
    Console.WriteLine("Треугольник не существует");
}