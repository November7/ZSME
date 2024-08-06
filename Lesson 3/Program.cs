/************************************************/
/*                Console.Write(Line)           */
/************************************************/


string imie = "Jan";
string nazwisko = "Nowak";


// Console.WriteLine(imie,nazwisko); // błędne użycie metody WriteLn (pierwszy argument to tekst formatowany, kolejne są opcjonalne, jako argumenty tekstu formatowanego)

Console.Write(imie);
Console.Write(" ");
Console.WriteLine(nazwisko);


Console.WriteLine("{0} {1}",imie,nazwisko); //każdy kod w postaci {nr} musi odpowiadać kolejnemu argumentowi, w przeciwnym wypadku nastąpi wyjątek
// Console.WriteLine("{0} {1} {2}",imie,nazwisko); //brak pokrycia dla argumentu {2} - wyjątek

// Tekst parsowany.

string output = $"{nazwisko} {imie}";
Console.WriteLine(output);

// Bez dodatkowej zmiennej

Console.WriteLine($"Nazwisko: {nazwisko}, Imię: {imie}");