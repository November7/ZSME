class App
{
    static int fun(int a, int b)
    {
        return a + b;
    }



    static int fun(int a, int b, out int c)
    {
        c = 123;
        return a + b + c;
    }

    static int Main()
    {
            Console.WriteLine(fun(3,4));
            int x;
            Console.WriteLine(fun(1,2,out x));
            Console.WriteLine(x);
            return 0;
    }


}

