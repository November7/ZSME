namespace StudentManagement
{
    class Student
    {
        private string name;
        private string sname;

        public Student()
        {
            name = "";
            sname = "";
        }

        public Student(string n, string s)
        {
            Name = n;
            Sname = s;
        }

        public string Name 
        { 
            get {return name;}
            set {name = value[0].ToString().ToUpper() + value.Substring(1).ToLower();}
        }
        
        public string Sname 
        { 
            get {return sname;}
            set {sname = value[0].ToString().ToUpper() + value.Substring(1).ToLower();}
        }

        public void PrintStudent()
        {
            Console.WriteLine($"{Name} {Sname}");
        }
        
    }
    class Program
    {
        public static List<Student> students = new();
        static void Main(string[] args)
        {
            
            Student nowy = new();
            nowy.Name = "janusz";
            nowy.Sname = "kowalski";
            students.Add(nowy);
            students.Add(new Student("katarzyna", "nowak"));

            foreach (var student in students)
            {
                student.PrintStudent();
            }
            // Console.WriteLine(nowy.Name);
        }
    }
}