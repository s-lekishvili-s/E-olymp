using System;

namespace Problem4
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            string setir = Console.ReadLine();
            var massiv = setir.Split(' ');
            double x1 = double.Parse(massiv[0]);
            double y1 = double.Parse(massiv[1]);
            double r1 = double.Parse(massiv[2]);
            double x2 = double.Parse(massiv[3]);
            double y2 = double.Parse(massiv[4]);
            double r2 = double.Parse(massiv[5]);
            var mesafe = Math.Sqrt((x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2));
            var cr = r1 + r2;
            var fr = Math.Abs(r1 - r2);
            if (mesafe == cr) Console.WriteLine("1");
            else
                if (mesafe > cr) Console.WriteLine("0");
                else
                    if (mesafe==0) Console.WriteLine(Math.Abs(r1 - r2) < double.Epsilon ? "-1" : "0");
                    else
                        if ((0 < mesafe) && (mesafe < cr))
                        {
                            if (fr < mesafe) Console.WriteLine("2");
                            else
                                if (fr==mesafe) Console.WriteLine("1");
                                else
                                    if (fr > mesafe) Console.WriteLine("0");
            }
        }
    }
}