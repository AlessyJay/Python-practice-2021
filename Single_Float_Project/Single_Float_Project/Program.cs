using System;

namespace Single_Float_Project
{
    class Program
    {
        static void Main(string[] args)
        {
            //Real number is pi = 3.14
            //e = 2.71

            string BinaryNumber;
            int Prodigy; // A sign bit
            string Lunis = ""; // Exponent
            int Caelestis; // Mantissa
            double Spectrum = 0; //A significant precision

            Console.Write("Enter your binary number here: ");
            BinaryNumber = Console.ReadLine(); //Make users be able to input numbers.

            char[] chars = BinaryNumber.ToCharArray(); //copy the characters in the instance to a unique array.
            int[] numbers = new int[chars.Length]; //To defined the length of Chars.
            for (int i = 0; i < chars.Length; i++)
            {
                numbers[i] = Int32.Parse((chars[i]).ToString()); //convert the number of 16 bits to it's equivalent strings.
            }
            if (numbers[0] == 0)
            {
                Prodigy = 1; //A sign bit = 1
            }
            else
            {
                Prodigy = -1; 
            }
            for (int i = 9; i < chars.Length; i++)
            {
                Spectrum = Spectrum + (numbers[i] * (Math.Pow(2, -double.Parse((i - 8).ToString())))); //Converts the value of the specified double-precision floating-point number to its equivalent string.
            }
            for (int i = 1; i < 9; i++)
            {
                Lunis = Lunis + chars[i];
            }

            Caelestis = (Convert.ToInt32(Lunis, 2) - 127);

            Console.WriteLine(((Prodigy * 1) + Spectrum) * Math.Pow(2, double.Parse(Caelestis.ToString())));
            Console.WriteLine("{0} x 2 e{1}", (Prodigy * (1 + Spectrum)).ToString(), Caelestis.ToString());
            Console.ReadKey();
        }
    }
}
