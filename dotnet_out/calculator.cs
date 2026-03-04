using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("=== Simple C# Calculator ===");

        Console.Write("Enter first number: ");
        double a = Convert.ToDouble(Console.ReadLine());

        Console.Write("Enter operator (+, -, *, /): ");
        string op = Console.ReadLine();

        Console.Write("Enter second number: ");
        double b = Convert.ToDouble(Console.ReadLine());

        double result = 0;

        switch (op)
        {
            case "+":
                result = a + b;
                break;
            case "-":
                result = a - b;
                break;
            case "*":
                result = a * b;
                break;
            case "/":
                if (b != 0)
                {
                    result = a / b;
                }
                else
                {
                    Console.WriteLine("Cannot divide by zero");
                    Environment.Exit(0);
                }
                break;
            default:
                Console.WriteLine("Invalid operator");
                Environment.Exit(0);
                break;
        }

        Console.WriteLine("Result = " + result);
    }
}