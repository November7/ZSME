int i; //uwaga na zasięg i czas życia zmiennej
i = 123;

if(i == 321)
{
    Console.WriteLine("Warunek 1 spełniony");
}
else if(i == 123)
{
    Console.WriteLine("Warunek 2 spełniony");
}
else
{
    Console.WriteLine("Warunek nie spełniony");
}

Console.WriteLine(i>10?"TAK":"NIE");

var s = "test";

switch(s)
{
    default:
    Console.WriteLine("Warunek domyślny spełniony");
    break;  //break obowiązkowy!!
    case "test":
    Console.WriteLine("Warunek 1 spełniony");
    break;
    case "set":
    Console.WriteLine("Warunek 2 spełniony");
    break;
}

for(i=0 ; i < 10 ; i++)
{
    Console.Write($"{i}, ");
}
Console.WriteLine();

i = 0;

while(i < 10)
{
    Console.Write($"{i}, ");
    i++;
}
Console.WriteLine();
i=0;
do
{
    Console.Write($"{i}, ");
    i++;
}while(i < 10);
Console.WriteLine();

int[] table = {1,2,3,4};

foreach(var item in table)
{
    Console.Write($"{item}, ");
}

Console.WriteLine();

int[] table2 = new int[123];
foreach(var item in table2)
{
    Console.Write($"{item}, ");
}

Console.WriteLine();