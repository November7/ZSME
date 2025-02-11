namespace SettersAndGetters
{

    class Osoba
    {
        private int zachowanie;
        private int matematyka;

        public int Matematyka
        {
            get { return matematyka; }
            set { 
                
                if (value < 1) matematyka = 1;
                else if (value > 6) matematyka = 6;
                else  matematyka = value; 
            }
        }

        public string Zachowanie
        {
            get { return zachowanie.ToString(); }
            set 
            { 
                if (value == "nagana") zachowanie = 1;
                else if (value == "dostateczne") zachowanie = 2;
                else if (value == "dobre") zachowanie = 3;
                else if (value == "bardzo dobre") zachowanie = 4;
                else if (value == "wzorowe") zachowanie = 5;
                else if (value == "celujące") zachowanie = 6;
                else zachowanie = 0;
            }
        }

        private string persel;

        public string PESEL
        {
            get { return persel; }
            init { persel = value; }
        }

        public Osoba(string p)
        {
            persel = p;
        }
    }

    class App
    {
        static void Main()
        {
            Osoba oceny = new Osoba("12345678901");
            oceny.Matematyka = 5;
            oceny.Zachowanie = "dobre";
            // oceny.PESEL = "12345678901";

            System.Console.WriteLine("Ocena z matematyki: " + oceny.Matematyka);
            System.Console.WriteLine("Ocena z zachowania: " + oceny.Zachowanie);
            System.Console.WriteLine("PESEL: " + oceny.PESEL);

        }
    }

}