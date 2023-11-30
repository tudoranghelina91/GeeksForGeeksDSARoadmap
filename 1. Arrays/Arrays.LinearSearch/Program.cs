int[] arr = new int[20];

Console.WriteLine("Elements in array: ");

for (int i = 0; i < arr.Length; i++)
{
    arr[i] = Random.Shared.Next(1, 100);
    Console.Write($"{arr[i]}");
    if (i < arr.Length - 1)
    {
        Console.Write(", ");
    }
}

Console.WriteLine();

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