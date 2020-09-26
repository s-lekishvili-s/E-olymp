using System;

namespace Problem22
{
    internal class Program
    {
        private static int Guzgu(int x)
        {
            var y = x.ToString();
            string z = "";
            int len = y.Length;
            for (int i = 0; i < len; i++)
            {
                z = y[i] + z;
            }
            return int.Parse(z);
        }

        private static bool Sade(int x)
        {
            if ((x == 0) || (x == 1)) return false;
            if ((x == 2) || (x == 3)) return true;
            if (x%2 == 0) return false;
            int kok = (int) Math.Sqrt(x) + 1;
            for (int i = 3; i < kok; i = i + 2)
            {
                if (x%i == 0) return false;
            }
            return true;
        }

        public static void Main(string[] args)
        {
            string setir = Console.ReadLine();
            var massiv = setir.Split(' ');
            var a = int.Parse(massiv[0]);
            var b = int.Parse(massiv[1]);
            int say = 0;
            if (a > b)
            {
                say = a;
                a = b;
                b = say;
                say = 0;
            }
            for (int i = a; i <= b; i++)
            {
                if (Sade(i))
                {
                    if (Sade(Guzgu(i))) say++;
                }
            }
            Console.WriteLine(say);
        }
    }
}