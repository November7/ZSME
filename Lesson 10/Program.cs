class App
{

    class CPoint
    {
        private int x;
        public int X 
        {
            get 
            {
                return x;
            }
            set
            {
                Console.WriteLine("Setter X"); 
                if (value > 0)
                    x = value;
                else
                    x = 0;
            }
        }
        private int y;
        public int Y 
        {
            get 
            {
                return y;
            }
            set
            {
                Console.WriteLine("Setter Y"); 
                if (value > 0)
                    y = value;
                else
                    y = 0;
            }
        }    

        public CPoint(int x, int y)
        {
            X = x;
            Y = y;
        }

        public override string ToString()
        {
            return $"({X}, {Y})";
        }
        ~CPoint()
        {
            Console.WriteLine("Destructor");  
        }
    }

    static void Main()
    {

        CPoint point = new CPoint(1,2);
        point.X = 0;
        Console.WriteLine(point.ToString());

    

        
    }


}