// Виды методов 
// Вид 1

void Method1()
{
    Console.WriteLine("Автор ... А. Максаймер");
}
Method1();


// Вид 2
void Method2(string msg)
{
    Console.WriteLine(msg);
}
Method2("Текст");

void Method21(string msg, int count)
{
    int i = 0;
    while (i < count)
    {
        Console.WriteLine(msg);
        i++;
    }
}
Method21(msg: "Текст", count: 4);
Method21(count: 4, msg: "Новый текст");

//Вид 3 (возвращают но не принимают)

int Method3()
{
    return DateTime.Now.Year;
}

int year = Method3();
Console.WriteLine(year);

// Вид 4 (принимают и возвращают)

string Method4(int count, char text)
{
    int i = 0;
    string result = string.Empty;
    while (i < count)
    {
        result = result + text;
        i++;
    }
    return result;
}

string res = Method4(10, "asdf");
Console.WriteLine(res);

// Вид 4 (пример с for)

string Method4(int count, char text)
{

    string result = string.Empty;
    for (int i =0; i < count; i++)
    {
        result = result + text;
    }
    return result;
}

string res = Method4(10, "z");
Console.WriteLine(res);

// Вид 4 (цикл в цикле)

for (int i = 2; i < 10; i++)
{
    for (int j = 0; j = 10; j++)
    {
        Console.WriteLine($"{i} x {j} = {i * j}");
    }
    Console.WriteLine();
}


