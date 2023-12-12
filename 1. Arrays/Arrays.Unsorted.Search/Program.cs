// See https://aka.ms/new-console-template for more information
using Array.Utils;

int[] array = ArrayGenerator.GenerateRandom(10);

array.Print();

Console.WriteLine("Type in a value to search:");

int key = Convert.ToInt32(Console.ReadLine());

// For unsorted arrays, just loop through the array.
for (int i = 0; i < array.Length; i++)
{
    if (array[i] == key)
    {
        Console.WriteLine($"Element {key} found at position {i}");
        return;
    }
}

Console.WriteLine($"Element {key} not found");