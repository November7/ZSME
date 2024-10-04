class b
{
    public b()
    {
        Console.WriteLine("Klasa b");
    }
    public b(string s)
    {
        Console.WriteLine($"Klasa b, parametr: {s}");
    }
    public void test()
    {
        Console.WriteLine("Metoda test z klasy a");
    }
}


class a{

    static void Main(string[] args)
    {
        b zm = new b("dsd");
        zm.test();
    }


}
