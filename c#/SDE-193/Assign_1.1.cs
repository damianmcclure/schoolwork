using System;

class MainClass {
  public static string line1 = "Helen, thy beauty is to me";
  public static string line2a = "Like those Nicean ";
  public static string line2b = "barks of yore,";
  public static string line3 = "That gently, o'er a perfumed sea,";
  public static string line4word = "way-worn";
  public static string line5 = "to his own native beach.";

  public static void Main (string[] args) {
    Console.WriteLine(line1);
    // Concatenation
    Console.WriteLine(line2a+line2b);
    // Lowercase method
    Console.WriteLine(line3.ToLower());
    // Interpolation
    Console.WriteLine($"The weary, {line4word} wanderer bore");
    // Uppercase method & Replace method
    Console.WriteLine(line5.ToUpper().Replace("BEACH", "SHORE"));
  }
}
