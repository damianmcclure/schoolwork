using System;

class MainClass {
  public static void Main (string[] args) {
    Console.WriteLine("How many classes did you attend this semester? ");
    int numberOfClasses = Int32.Parse(Console.ReadLine());

    Console.WriteLine("\nFor the next questions, type A, B, C, D or F as your answer.");

    //I decided to use an array even though we haven't learned this yet, it's just easier for me.
    double[] classGrades = new double[numberOfClasses];

    for(int i = 0; i < numberOfClasses; i++){
      Console.WriteLine("Letter Grade for Class "+(i+1)+"? ");
      string temp = Console.ReadLine();
      if(temp == "A"){
        classGrades[i] = 4.0;
      } else if(temp == "B"){
        classGrades[i] = 3.0;
      } else if(temp == "C"){
        classGrades[i] = 2.0;
      } else if(temp == "D"){
        classGrades[i] = 1.0;
      } else if(temp == "F"){
        classGrades[i] = 0.0;
      } else {
        Console.WriteLine("Error, incorrect letter grade entered, try again.");
        i--;
      }
    }

    double total = 0.0;

    for(int i = 0; i < numberOfClasses; i++){
      total = total + classGrades[i];
    }

    double average = total/numberOfClasses;

    Console.WriteLine("Your GPA is: "+average.ToString());

    if(average >= 3.5){
      Console.WriteLine("You made the Dean's List, Congratulations!");
    } else if(average < 3.5 && average >= 2.0){
      //Nothing here, just to keep the if statement working
    } else {
      Console.WriteLine("You are unfortunately on Academic Probation.");
    }
  }
}
