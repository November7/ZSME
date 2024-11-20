class CExample
{
    private int x;

    public int X 
    {
        get
        {
            return x;
        }
        // init
        set
        {
            if(value>100)
                x = 100;
            else if(value<0)
                x = 0;
            else
                x = value;
        }
    }

    public CExample()
    {
        Console.WriteLine("Tworzę obiekt");
        x = 0;
    }
    
}

class App
{
    static void Main()
    {

        CExample ob = new();
        ob.X = 123;
        Console.WriteLine(ob.X);
        ob.X = -123;
        Console.WriteLine(ob.X);
        ob.X = 33;
        Console.WriteLine(ob.X);



       
    }
}