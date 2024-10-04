/************************************************/
/*                Console.WriteLine()           */
/************************************************/
// using System;

string imie = "Jan";
string nazwisko = "Nowak";

// v1 Console.Write()

Console.Write(imie); //bez znaku końca linii
Console.Write(" ");
Console.Write(nazwisko);
Console.Write("\n"); //znak końca linii

// v2 złączenie tekstów (konkatenacja)

Console.Write(imie + " " + nazwisko + "\n");

// v3 tekst formatowany (interpolacja tekstu):

string output = $"{imie} {nazwisko}\n"; //dodatkowa zmienna
Console.Write(output);

// lub bez dodatkowej zmiennej:
// Console.Write($"{imie} {nazwisko}\n");

// v4 WriteLine

Console.WriteLine($"{imie} {nazwisko}");

// v5 

Console.WriteLine("{0} {1}",imie,nazwisko);

// Console.WriteLine("{0} {1} {2}",imie,nazwisko); //brak pokrycia dla argumentu {2} - wyjątek


/************************************************/
/*                Console.ReadLine()            */
/************************************************/

Console.Write("Podaj liczbę: ");
string? inp = Console.ReadLine(); // typ nullable: <typ>?
        
// Console.WriteLine($"Wprowadzono: {inp}");
 
if (inp != null)
{
    Console.WriteLine($"Wprowadzono: {inp}");
}