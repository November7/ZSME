class App
{

    static void Main()
    {
        //Pętla for
      
        for (int i = 0; i < 10; i++)
        {
            Console.WriteLine($"Iteracja: {i}");
        }

        //Pętla while
        
        int j = 0;
        
        while (j < 10)
        {
            Console.WriteLine($"Iteracja: {j}");
            j++;
        }

        //Pętla do-while
        
        int k = 0;
        
        do
        {
            Console.WriteLine($"Iteracja: {k}");
            k++;
        } while (k < 10);


        //Pętla foreach

        int[] numbers = { 1, 2, 3, 4, 5 };
        
        foreach (int number in numbers)
        {
            Console.WriteLine($"Liczba: {number}");
        }

        string s = "Ala ma kota";

        foreach (char c in s)
        {
            Console.WriteLine($"Znak: {c}");
        }
        
        //Instrukcja break
        
        for (int i = 0; i < 10; i++)
        {
            if (i == 5)
            {
                break;
            }
            Console.WriteLine($"Iteracja: {i}");
        }

        //Instrukcja continue
        
        for (int i = 0; i < 10; i++)
        {
            if (i % 2 == 0)
            {
                continue;
            }
            
            Console.WriteLine($"Liczba: {i}");
            
        }

        //licznik pętli for, co zrobi break??

        int licznik;

        for (licznik = 0; licznik < 10; licznik++)
        {
            if(licznik == 5) break;

            Console.WriteLine($"Iteracja: {licznik}");
        }   
        Console.WriteLine($"Licznik po użyciu break: {licznik}");     
    }
}