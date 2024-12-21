
class App
{
    static void Main()
    {     
        // //String
        // string strTekst1 = "Jakiś przykładowy tekst";        
        // Console.WriteLine(strTekst1);
        
        // string strTekst2 = new string("Jakiś inny tekst");
        // Console.WriteLine(strTekst2);

        // char[] tChr = ['a','b','c','d','e','f'];
        // string strTekst3 = new string(tChr);
        // Console.WriteLine(strTekst3);

        // foreach (var item in strTekst1)
        // {
        //     Console.Write($"{item}, ");
        // }
        // Console.WriteLine();

        // strTekst1 += " z uzupełnieniem";

        // Console.WriteLine(strTekst1);
        // Console.WriteLine(strTekst1[0]);

        // //strTekst[0] = 'j'; // błąd
        // strTekst1 = 'j' + strTekst1.Substring(1);        
        // Console.WriteLine(strTekst1);

        // //Zastępowanie znaków:
        // strTekst1 = strTekst1.Replace('a', 'x');
        // Console.WriteLine(strTekst1);

        // //Parsowanie tekstu (interpolacja)
        // int nLiczba = 123;
        // DateTime teraz = DateTime.Now;
        Random random = new Random();

        // Console.WriteLine($"jakiś tekst zawierający formuły: {123 + 321}, {Math.Sqrt(nLiczba):N} {teraz: yyyy MM dddd} {random.Next(123)}");
        // // Console.WriteLine("jakiś tekst zawierający formuły: {0}, {1:N} {2: yyyy MM dddd} {3}",123+321,Math.Sqrt(nLiczba),teraz,random.Next(123));

        // //Ignorowanie znaków ucieczki
        // Console.WriteLine("C:\\windows\\system32\\");
        // Console.WriteLine(@"C:\windows\system32\");
        // Console.WriteLine(@"tekst który jest 
        //                     zapisany w kilku
        //                      liniach");

        // // Najważniejsze metody i właściwości String:

        // Console.WriteLine($"Długość tekstu: {strTekst1.Length}");
        // Console.WriteLine($"Fragment tekstu: {strTekst1.Substring(5)}, {strTekst1.Substring(3,7)}");
        // Console.WriteLine($"Pierwsze/ostatnie wystąpienie znaku: {strTekst1.IndexOf('a')}, {strTekst1.LastIndexOf('p')}");
        // Console.WriteLine($"Zawieranie tekstu: {strTekst1.Contains("tekst")} {strTekst1.Contains('a')}");
        // Console.WriteLine($"Zastępowanie tekstu: {strTekst1.Replace("tekst","TEKST")}");
        // Console.WriteLine($"Zwiększanie/Zmniejszanie tekstu: {strTekst1.ToLower()} {strTekst1.ToUpper()}");
        // Console.WriteLine($"Usuwanie białych znaków z początku i końca tekstu: {"    tekst ze spacjami    ".Trim()}");

        // //Podział tekstu na podteksty:
        // string[] podteksty = strTekst1.Split(" ");
        // foreach (var item in podteksty)
        // {
        //     Console.WriteLine($"{item}, ");
        // }     

        // Console.WriteLine($"Łączenie tekstów: {string.Join("|",podteksty)}");
        // Console.WriteLine($"Konkatenacja: {string.Concat("jeden tekst"," ---- ","trzeci tekst")}");
        // Console.WriteLine($"Formatowanie tekstu: {string.Format(" {0:C}, {1:x04}, {1:b010}", 123.321, 123)}");
               
        // Tablica

        int[] arrLiczby = new int[10];

        for (int i = 0; i < 10; i++)
        {
            arrLiczby[i] = random.Next(10);
        }

        foreach (var item in arrLiczby)
        {
            Console.Write($"{item}, ");
        }
        Console.WriteLine();

        // arrLiczby[10] = 123; //wyjątek!!!
        
        int[] arrLiczby2 = {1, 3, 4, 3, 5, 6, 7, 3, 3, 5, 7, 4, 3};
        // int[] arrLiczby2b = new int[13] {1, 3, 4, 3, 5, 6, 7, 3, 3, 5, 7, 4, 3};

        foreach (var item in arrLiczby2)
        {
            Console.Write($"{item}, ");
        }
        Console.WriteLine();

        int[] arrLiczby3 = [1, 3, 4, 3, 5, 6, 7, 3, 3, 5, 7, 4, 3];

        foreach (var item in arrLiczby3)
        {
            Console.Write($"{item}, ");
        }
        Console.WriteLine();

        // tablice wielowymiarowe

        int[,] arrMatrix1 = new int[3, 4];
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                arrMatrix1[i, j] = random.Next(10);                
            }
        }

        int [,] arrMatrix2 = {{1,2,3},{4,5,6}};

        for (int i = 0; i < 2; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                Console.Write($"{arrMatrix2[i, j]},");
            }
            Console.WriteLine();
        }
        
        foreach (var item in arrMatrix2)
        {
            Console.Write($"{item},");
        }
        Console.WriteLine();


        //tablice postrzępione (tablice tablic)

        int[][] arrJagged0 = { new int[2], new int[5]}; 
        int[][] arrJagged1 = { new int[2] {1,2}, new int[5] {1,3,2,4,5}};
        int[][] arrJagged2 = { new int[] {1,2}, new int[] {1,3,2,4,5}};

        foreach (int[] arr in arrJagged1)
        {
            foreach (int item in arr)
            {
                Console.Write($"{item}, ");
            }
            Console.WriteLine();
        }       


        int[][] arrJagged3 = [[1,2], [1,3,2,4,5]];

        // int[][] arrJagged3 = {{1,2,3},{4,5,6}}; //niepoprawnie

        int[] t1 = {1,2,3,4,5,6};
        int[] t2 = t1;
        int[] t3 = new int [6];
        Array.Copy(t1,t3,6);

        for (int i = 0; i < t1.Length; i++)
        {
            Console.Write($"{t1[i]}, ");         
        }
        Console.WriteLine();
        for (int i = 0; i < t2.Length; i++)
        {         
            Console.Write($"{t2[i]}, ");
        }
        Console.WriteLine();
        for (int i = 0; i < t3.Length; i++)
        {         
            Console.Write($"{t3[i]}, ");
        }
        Console.WriteLine();

        t1[0] = 123;

        for (int i = 0; i < t1.Length; i++)
        {
            Console.Write($"{t1[i]}, ");         
        }
        Console.WriteLine();
        for (int i = 0; i < t2.Length; i++)
        {         
            Console.Write($"{t2[i]}, ");
        }
        Console.WriteLine();
        for (int i = 0; i < t3.Length; i++)
        {         
            Console.Write($"{t3[i]}, ");
        }
        Console.WriteLine();

        //CopyTo
        
        int[] t4 = new int[10];
        t3.CopyTo(t4, 3); 
        for (int i = 0; i < t4.Length; i++)
        {         
            Console.Write($"{t4[i]}, ");
        }
        Console.WriteLine();

        Array.Sort(t4);
        Array.Reverse(t4);
        
        for (int i = 0; i < t4.Length; i++)
        {         
            Console.Write($"{t4[i]}, ");
        }
        Console.WriteLine();

        Console.WriteLine($"Pierwsze/ostatnie wystąpienie wartości: {Array.IndexOf(t4,3)} {Array.IndexOf(t4,332)} {Array.LastIndexOf(t4,3)}");        
    }
}
