using System;

class MainClass {
  // IncreasedCost function, takes dollarvalue and a percentage in the form of a decimal.
  public static double IncreasedCost(double dollarvalue, double percentage){
    return dollarvalue * percentage;
  }

  public static void Main (string[] args) {
    while(true){
      // Employee Pay Array
      double[] employeePay = {35000, 38000, 40000, 47000, 59000};

      // Informing user to write percentage like a decimal.
      Console.WriteLine("What percentage to raise the employees pays by? (Note: write it in decimal form, so 5% will be 0.05)");

      // Parsing the number with Double.Parse this time.
      string userinput = Console.ReadLine();

      if(!userinput.Contains(".")){
        Console.WriteLine("Incorrect percentage entered.");
        continue;
      }

      double percent = Double.Parse(userinput);

      double totalCost = 0;

      // Doing the Calculations.
      totalCost = totalCost + IncreasedCost(employeePay[0], percent);
      totalCost = totalCost + IncreasedCost(employeePay[1], percent);
      totalCost = totalCost + IncreasedCost(employeePay[2], percent);
      totalCost = totalCost + IncreasedCost(employeePay[3], percent);
      totalCost = totalCost + IncreasedCost(employeePay[4], percent);
                
      // Writing the answer.
      Console.WriteLine($"The total cost of a 5% raise is ${totalCost}");

      // Asking the user if they want to do more calculations.
      Console.WriteLine("Do you want to do more calculations? (Yes/No)");
      string answer = Console.ReadLine();
      if(answer == "No"){
        break;
      }
    }
  }
}
