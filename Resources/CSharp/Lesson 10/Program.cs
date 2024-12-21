class CExample
{
    private int x;

    public int X
    {
        set
        {
            if(value > 100)     x = 100;
            else if (value < 0) x = 0;    
            else                x = value;
        }
        get
        {
            return x;
        }
    }

    public CExample()
    {
        X = 0;
        Console.WriteLine("Obiekt jest tworzony");
    }    
}

class App
{
    static void Main()
    {
        CExample ob = new();
        ob.X = 123;
        Console.WriteLine($"{ob.X}");
    }
}