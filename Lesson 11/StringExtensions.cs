namespace StringExtensions
{
    
    static class CStringExtensions
    {
        public static string Capitalize(this string obj)
        {
            return obj[0].ToString().ToUpper() + obj.Substring(1).ToLower();
        }

        public static string Title(this string obj, string sep = " ")
        {
            string[] parts = obj.Split(sep);
            for(int i = 0 ; i<parts.Length; i++)
            {
                parts[i] = parts[i].Capitalize();
            }

            return string.Join(sep,parts);
        }
    }


}