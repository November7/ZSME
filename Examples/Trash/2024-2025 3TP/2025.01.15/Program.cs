class CExaple
{
    public CExaple()
    {
        Pole = 0;
    }

   

    private int pole = 1;
    public int Pole
    {
        get
        {
            return pole;
        }
        set
        {
            if (value < 0)
            {
                pole = 0;
            }
            else
            {
                pole = value;
            }
        }
    }

    public override string ToString()
    {
        return $"{Pole}";  

    }
}

namespace app
{
    class Program
    {
        static void Main(string[] args)
        {
            CExaple obj = new();
            obj.Pole = -5;
            Console.WriteLine(obj);
        }
    }
}
