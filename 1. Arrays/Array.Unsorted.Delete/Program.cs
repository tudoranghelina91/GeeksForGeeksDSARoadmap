// See https://aka.ms/new-console-template for more information
using Array.Utils;

Console.WriteLine("Hello, World!");

int[] arr = ArrayGenerator.GenerateSequential(10, 1, 10);

arr.Print();

Console.WriteLine("Pick an item to delete:");

int elementToRemove = Convert.ToInt32(Console.ReadLine());
int n = arr.Length;

int i = 0;

while (i < n)
{
    if (arr[i] == elementToRemove)
    {
        for (int j = i; j < arr.Length - 1; j++)
        {
            arr[j] = arr[j + 1];
        }

        n--;
        break;
    }

    i++;
}

if (n == arr.Length)
{
    Console.WriteLine($"Element {elementToRemove} not found");
}

arr.Print(n);

