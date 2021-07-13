using System;

namespace Parity_Project
{
    class Program
    {
        static void Main(string[] args)
        {
            int ParityGiven;
            int ParityCalculated;
            int CounterCheck = 0; //if the result = 0.
            bool checks; //check the parity if it's true or false (even or odd).
            Console.WriteLine("Enter your parity here: ");
            string BinaryNumber = Console.ReadLine(); // Make users to be able to input the binary number here.

            char[] Chars = BinaryNumber.ToCharArray(); //copy the characters in the instance to a unique array.
            int[] Numbers = new int[Chars.Length]; //To defined the length of Chars.
            for (int i = 0; i < Chars.Length; i++)
            {
                Numbers[i] = Int32.Parse((Chars[i]).ToString()); //convert the number of 16 bits to it's equivalent strings.
            }
            ParityGiven = Numbers[Chars.Length - 1];
            for (int i = 0; i < Chars.Length - 1; i++)
            {
                if (Numbers[i] == 1)
                {
                    CounterCheck++;
                }
                else
                {
                    // This means do nothing...
                }
            }
            if (CounterCheck % 2 == 0)
            {
                ParityCalculated = 0;
            }
            else { ParityCalculated = 1; }
            checks = (ParityCalculated == ParityGiven);
            if (checks)
            {
                Console.WriteLine("Your parity is an even!");
            }
            if (!checks)
            {
                Console.WriteLine("Your parity is an odd!");
            }
            Console.ReadKey();
        }
    }
}
