// Question 3: make a function that multiplies 3 numbers & call it using 3, 5, and 10 as the arguments.
using System;

namespace MidTerm
{
    class Program
    {
        // The simple multiply function
        static int multiply(int num1, int num2, int num3)
        {
            return num1 * num2 * num3;
        }
        static void Main(string[] args)
        {
            // Calling the function with 3, 5, and 10, and printing it.
            int answer = multiply(3, 5, 10);
            Console.WriteLine(answer);
        }
    }
}
