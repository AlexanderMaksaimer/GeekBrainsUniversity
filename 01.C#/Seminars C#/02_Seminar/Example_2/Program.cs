// Вывести на экран первую и третью цифру из трехзначного числа
int number = new Random ().Next(100,1000);
string strr = number.ToString();

Console.WriteLine($"{number} -> {strr[0]}{strr[2]}");