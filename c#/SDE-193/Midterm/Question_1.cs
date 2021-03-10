// Question 1: print happy birthday as many times as their age.

using System;

namespace MidTerm
{
    class Program
    {
        static void Main(string[] args)
        {
            // Asks the user their age.
            Console.WriteLine("Hello, how old are you?");
            int age = Int32.Parse(Console.ReadLine());
            for(int i = 0; i < age; i++)
            {
                // Loops through and writes it the amount of times.
                Console.WriteLine("Happy Birthday!");
            }
        }
    }
}
