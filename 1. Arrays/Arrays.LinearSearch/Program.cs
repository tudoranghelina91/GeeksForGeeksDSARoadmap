using Array.Utils;

int[] arr = ArrayGenerator.GenerateRandom();
arr.Print();

Console.WriteLine("Type in a number to search for: ");

int key = Convert.ToInt32(Console.ReadLine());

for (int i = 0; i < arr.Length; i++)
{
    if (arr[i] == key)
    {
        Console.WriteLine($"Element {key} found at position {i}");
        return;
    }
}

Console.WriteLine($"Element {key} not found.");