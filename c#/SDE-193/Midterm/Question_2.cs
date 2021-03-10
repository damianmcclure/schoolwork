// Question 2: if they own a common pet, print that they do, otherwise print that they have a unique animal.
using System;
// System.Linq required for Array.Contains();
using System.Linq;

namespace MidTerm
{
    class Program
    {
        static void Main(string[] args)
        {
            // Creating array for the common types of animals.
            string[] common = { "cat", "dog", "fish" };
            // Asking what pet they own.
            Console.WriteLine("What kind of pet do you own?");
            string pet = Console.ReadLine();
            // Checking if users input is in the common animals array.
            if (common.Contains(pet))
            {
                // Response if it is common.
                Console.WriteLine("A " + pet + " is good common pet.");
            } else
            {
                // Response if it is not common.
                Console.WriteLine("Wow, a " + pet + ", what a unique animal!");
            }
        }
    }
}
