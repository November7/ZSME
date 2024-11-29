namespace Point
{
    public class CPoint
    {
        private double x, y;
        public double X
        {
            get { return x; }
            set { x = value; }
        }

        public double Y
        {
            get { return y; }
            set { y = value; }
        }
        public CPoint()
        {
            Console.WriteLine("CPoint");
            x = 0;
            y = 0;
        }
        public CPoint(double x, double y)
        {
            this.x = x;
            this.y = y;
        }
        public override string ToString()
        {
            return $"({x}, {y})";
        }
        ~CPoint()
        {
            Console.WriteLine("Niszczenie obiektu");
        }

    }


    public class CPoint3D : CPoint
    {
        private double z;
        public double Z { get; set; }
        public CPoint3D() : base()
        {
            Console.WriteLine("CPoint3D");
            z = 0;
        }

        ~CPoint3D()
        {
            Console.WriteLine("Niszczenie obiektu 3D");
        }

        public override string ToString()
        {
            return $"({base.X}, {base.Y}, {Z})";
        }
    }
}

