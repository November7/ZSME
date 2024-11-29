namespace Fraction
{
    class CFraction
    {
        private int numerator = 0;
        private int denominator = 1;

        public int Numerator 
        { 
            get { return numerator; }
            set { numerator = value; }
        }
        public int Denominator
        {
            get { return denominator; }
            set { denominator = value != 0 ? value : 1; }
        }

        public CFraction()
        {
            numerator = 0;
            denominator = 1;
        }

        public CFraction(int numerator, int denominator) : this()
        {
            this.numerator = numerator;
            if(denominator != 0) this.denominator = denominator;
        }

        public override string ToString()
        {
            int sign = 1;
            if (Denominator < 0)
                sign = -1;
            string denom;
            denom = sign * Denominator != 1 ? "/" + (sign * Denominator).ToString() : "";
            return $"{sign*Numerator}{denom}";
        }

        public static CFraction operator* (CFraction A, CFraction B)
        {
            CFraction result = new();
            result.Numerator = A.Numerator * B.Numerator;        
            result.Denominator = A.Denominator * B.Denominator;
            
            return result;
        }

        public static CFraction operator++(CFraction A)
        {
            A.Numerator+=A.Denominator;
            return A;
        }
    }
}
