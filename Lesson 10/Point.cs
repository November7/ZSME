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

    }


    public class CPoint3D : CPoint
    {
        private double z;
        public double Z { get; set; }
        public CPoint3D() : base()
        {
            z = 0;
        }

        public override string ToString()
        {
            return $"({base.X}, {base.Y}, {Z})";
        }
    }
}

