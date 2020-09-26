using System;

namespace Test
{
    class Problem10
    {
        public static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            double vedre = 0;
            var saygac = n;
            int k = 0;
            while (vedre<=0.5)
            {
                vedre = vedre + 1.0/saygac;
                k++;
                saygac = saygac - 1;
            }
            Console.WriteLine(n-k+1);
        }
    }
}