

// // Console.WriteLine(fun(1,2));
// // Console.WriteLine(fun(1,2,3));

// string inp = Console.ReadLine();
// Console.WriteLine(inp);

// // try{

// // }
// // catch (Exception e)
// // {
// //     Console.WriteLine($"Wystąpił wyjątek: {e.Message}");
// // }
// // 

// int liczba;
// int.TryParse(inp,out liczba);

// // int liczba = int.Parse(inp);
// // int.TryParse(inp, out liczba);

// Console.WriteLine($"Liczba podana: {liczba}");


// // int x = 123;
// // int y = 5321;


// // x^=y^=x^=y;
// // Console.WriteLine(x^=y);
// // Console.WriteLine(y^=x);
// // Console.WriteLine(x^=y);



// // Console.WriteLine($"x: {x}, y: {y}");

// // double pi = Math.PI;
// // double r = 123;
// // Console.Write("Podaj promień koła:  ");
// // r = Convert.ToDouble(Console.ReadLine());

// // int pole = Convert.ToInt32(2*pi*r);

// // Console.WriteLine($"Obwód koła o promieniu {r} wynosi: {pole}");

// // var x = 3;
// // // x = 3.5;

// // Console.WriteLine(x);


class Program
{
    static void Main()
    {
        // Przekierowanie standardowego wejścia z pliku
        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);

            string line;
            while ((line = Console.ReadLine()) != null)
            {
                Console.WriteLine(line);
            }
        }
    }
}