namespace LocalFunctions
{
    class App
    {
        static void Main()
        {   
            int x = 3, y = 4;

            System.Console.WriteLine(Add(x, y));

            int Add(int a, int b)
            {
                return a + b;
            }

            int zmienna; //zmienna niezainicjowana
            Init(out zmienna, 101);

            System.Console.WriteLine(zmienna);

            void Init(out int val, int v)
            {
                //można tylko przypisywać wartość do zmiennej val.
                if(v<0) val = 0;
                else if (v>100) val = 100;
                else val = v;
                
            }

            int a = 5; //zmienna musi być zainicjowana
            Inc(ref a);
            System.Console.WriteLine(a);

            void Inc(ref int a)
            {
                a++;    //można modyfikować wartość (np. inkrementować)
            }

        }
    }
}