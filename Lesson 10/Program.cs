class CExample
{
    private int a;
    public int A 
    {
        get
        {
            return a;
        } 
        init
        {
            a = value;
            Console.WriteLine("inicjalizacja A");
        }
        // set
        // {
        //     if (value < 0)
        //     {
        //         a = 0;
        //     }
        //     else a = value;
        // }
    }

    public CExample()
    {
        A = 123;
        Console.WriteLine("Hi");
    }
    ~CExample()
    {
        Console.WriteLine("Bye");
    }
    public virtual void PrintA()
    {
        Console.WriteLine(A);
    }
}



class App
{
    static void Main()
    {
        CExample example = new CExample();
        // example.A = 10;
        example.PrintA();

       
    }
}