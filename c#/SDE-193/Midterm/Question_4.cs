// Question 4 : Write a program with a specified array and change all the numerical items to their word counterparts.
using System;

namespace MidTerm
{
    class Program
    {
        static void Main(string[] args)
        {
            // Array of the strings given.
            string[] numbers = { "ten", "9", "9", "ten", "9" };
            // Array to be filled later with new information.
            string[] newnumbers = { "", "", "", "", ""};
            // Looping for the length of the numbers array.
            for(int i = 0; i < numbers.Length; i++) 
            {
                Console.WriteLine(numbers[i]);
                string newnumber;
                // Checking if it is "9" or not.
                if(numbers[i] == "9")
                {
                    newnumber = "nine";
                } else
                {
                    newnumber = numbers[i];
                }
                // Adding new number to the new array.
                newnumbers[i] = newnumber;
            }
            Console.WriteLine("\n");
            foreach(string newnumber in newnumbers)
            {
                // Printing each number in the new array.
                Console.WriteLine(newnumber);
            }
        }
    }
}
