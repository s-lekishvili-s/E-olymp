using System;

namespace Problem920
{
    internal class Program
    {
        private static double Min(double a, double b, double c)
        {
            var kicik = a < b ? a : b;
            if (c < kicik) kicik = c;
            return kicik;
        }

        private static double Max(double a, double b)
        {
            return a > b ? a : b;
        }

        public static void Main(string[] args)
        {
            string setir = Console.ReadLine();
            var massiv = setir.Split(' ');
            double x = double.Parse(massiv[0]);
            double y = double.Parse(massiv[1]);
            double z = double.Parse(massiv[2]);
            Console.WriteLine("{0:N2}", Min(Max(x, y), Max(y, z), x + y + z));
        }
    }
}