namespace SettersAndGetters
{
    class Osoba
    {
        private int zachowanie;
        private int matematyka;
        private string pesel;

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
            get 
            { 
                  if(zachowanie == 1) return "Naganne";
                  else if(zachowanie == 2) return "Nieodpowiednie";
                  else if(zachowanie == 3) return "Poprawne";
                  else if(zachowanie == 4) return "Dobre";
                  else if(zachowanie == 5) return "Bardzo dobre";
                  else if(zachowanie == 6) return "Wzorowe";
                  else return "Brak oceny";
            }
            set
            {
                if (value == "naganne") zachowanie = 1;
                else if (value == "nieodpowiednie") zachowanie = 2;
                else if (value == "poprawne") zachowanie = 3;
                else if (value == "dobre") zachowanie = 4;
                else if (value == "bardzo dobre") zachowanie = 5;
                else if (value == "wzorowe") zachowanie = 6;
                else zachowanie = 0;
            }
        }


        public string PESEL
        {
            get { return pesel; }
            init { pesel = value; }
        }

        public Osoba(string p)
        {
            PESEL = p;
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