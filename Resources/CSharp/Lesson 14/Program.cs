namespace AnonymouseFunctions
{
    class App
    {
        static void Main()
        {
            Action<int, int> Add = delegate(int a, int b)
            {
                Console.WriteLine(a + b);    
            };


            Add(3, 4);

            Func<int, int, float> Mean = delegate(int a, int b)
            {
                return (a + b) / 2.0f;
            };

            Console.WriteLine(Mean(3, 4));


            Func<int, int, int, float> Avg = (a, b, c) => (a + b + c) / 3.0f;

            Console.WriteLine(Avg(3, 4, 5));

            int lokalnaFunkcja(int a, int b)
            {
                return a + b;
            }

            Func<int, int, int> uchwyt = lokalnaFunkcja;


            Console.WriteLine(uchwyt(3, 4));

            void Wypisz(int a)
            {
                Console.WriteLine(a);
            }

            Func<int, int, Action> test = delegate(int a, int b)
            {
                Action ret = () => Wypisz(a + b);
                return ret;
            };

            test(3, 4)();



        }
    }
}