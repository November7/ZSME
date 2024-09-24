using System.ComponentModel.Design;

int[] t = {1,2,5,3,2,4,65,7,4,3,2,2,24,6,7};

var result = from item in t where item != 1 select item;

foreach(var it in result)
{
    Console.WriteLine(it);
}