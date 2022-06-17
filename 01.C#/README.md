##Запуск проекта:

Создаём папку

Открываем её в новом терминале ( или проходим в неё через открытый терминал)

Пишем команду: 

>dotnet new console

Начинаем работать

Для теста может сразу прописать команду 

>dotnet run

Или сразу начать писать код

# Синтаксис:

<details><summary>Полезные фишки</summary>
<p>

```C++
Console.Clear(); /* Очистка терминала ( экрана) */
Console.ReadLine();/* В конце программы ожидает ENTER */
```

</p>
</details>

<details><summary>Вывод текста</summary>
<p>

```C++
/* Печать без перехода на новую строку*/
Console.Write("Text");
/* Печать с преходом на новую строчку*/
Console.WriteLine("Text");
Console.Write("Text\n"); /* внутири \n используется как перенос строки */
Write($"Text {name} and {age}") /* выводит текст и использует параметры */
Write($"Text {0} and {1}",name , age) /* выводит текст и использует параметры */
Write("Text - " + a + " Next - " + b)
```

</p>
</details>

<details><summary>Ввод</summary>
<p>

```C++
Console.ReadLine(); /* Вводит СТРОЧКУ введённую в терминал */
/* ВАЖНО! ввод всегда строчный! */
int a = int.Parse(Console.ReadLine()); /* То что вводится перевожится в int */
int a = Convert.ToInt(Console.ReadLine()); /* То что вводится перевожится в int */
Console.ReadKey(); /* Вроде как собирает нажатие кнопки */
/* Схема записи нажатия кнопки */
Console.WriteLine("Press a Button");
ConsoleKeyInfo but = Console.ReadKey();
Console.WriteLine(but.Key.ToString());
```

</p>
</details>

<details><summary>Массивы и списки</summary>
<p>

### Массивы:

```C++
/* Создание массива */
int[] array = new int[10];
int[] array1 = new int[] { 1, 3, 5, 7, 9 };
/* Замена или вывод */
array[0] = 20;
Console.WriteLine(array[1]);
/* Длина массива */
array.Length
```

### Списки:

```C++
/* Создание списка */
List<string> people = new List<string>(16);
List<string> people = new List<string>(){"Tom","Bill","Kate",};
/* Добавление эллемента в список */
people.Add("Bob");/* Вставляет в конец */
people.Incert(0,"Bob");/* Вставляет в начало */
/* Удаление эллемента из списока */
people.RemoveAt(1)/* Удалаяет эллемент под индексом 1*/
people.Remove("Tom")/* Удалаяет эллемент Том*/
/* Поиск эллемента */
people.Contains("Bob") /* Проверяет есть ли в списке Боб */
people.Exists(p => p.Length == 3)/* Проверяет если ли эллемент длиной 3 символа */
people.Find(p => p.Length == 3)/* Находит первого у кого в эллементе 3 символа */
people.FindAll(p => p.Length == 3)/* Находит всех у кого в эллементе 3 символа */
/* Длина списка */
people.Count /* Длина списка */
```

</p>
</details>

<details><summary>IF синтаксис</summary>
<p>

```C++
/* Стандартный вариант */
if ( a > b )
{
   Console.Write($" {a} > {b}");
}
else if ( a < b )
{
   Console.Write($" {a} < {b}");
}
else
{
   Console.Write($" {a} = {b}");
}
/* Короткий вариант */
if ( a > b ) Console.Write($" {a} > {b}");
else if ( a < b ) Console.Write($" {a} < {b}");
else Console.Write($" {a} = {b}");
/* Особый вариант */
int z = x < y ? (x+y) : (x-y)/* Нужно практиковаться - если True первая формула, если false вторая */

```

</p>
</details>

<details><summary>WHILE синтаксис</summary>
<p>

```C++
while ( i < length)
{
   Console.WriteLine("Test {i}");
   i++;
}

```

</p>
</details>

<details><summary>FOR синтаксис</summary>
<p>

```C++
/* Цикл стандартный */
for (int i = 0; i<length ; i++)
{
   Console.WriteLine("Test {i}");
}
/* Цикл не стандартный */
for (Console.WriteLine("Начало выполнения цикла"); i < 4; Console.WriteLine($"i = {i}"))
{
    i++;
}
for (int i = 1, j = 1; i < 10; i++, j++)
    Console.WriteLine($"{i * j}");

```

</p>
</details>

<details><summary>DO WHILE синтаксис</summary>
<p>

```C++
/* Схема цикла */
int i = 6;
do
{
    Console.WriteLine(i);
    i--;
}
while (i > 0);
```

</p>
</details>

<details><summary>FOREACH синтаксис</summary>
<p>

```C++
/* Схема цикла */
foreach(char c in "Tom")
{
    Console.WriteLine(c);
}
```

</p>
</details>

<details><summary>Смена цвета текста</summary>
<p>

```C++
Console.ForegroundColor = ConsoleColor.Green; // устанавливаем цвет
Console.WriteLine("...");
Console.ResetColor(); // сбрасываем в стандартный
```

</p>
</details>