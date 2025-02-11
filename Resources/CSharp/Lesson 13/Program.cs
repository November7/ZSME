namespace LocalFunctions
{
    class App
    {
        static void Main()
        {
            System.Console.WriteLine(Add(2, 3));

           
            int Add(int a, int b)
            {
                return a + b;
            }

            int zmienna;
            Init(out zmienna, 101);

            System.Console.WriteLine(zmienna);


            void Init(out int val, int v)
            {
                if(v<0) val = 0;
                else if (v>100) val = 100;
                else val = v;
                
            }

            int a = 5;
            Inc(ref a);
            System.Console.WriteLine(a);

            void Inc(ref int a)
            {
                a++;
            }

        }
    }
}