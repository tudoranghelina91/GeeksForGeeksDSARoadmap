// See https://aka.ms/new-console-template for more information
using Array.Utils;

Console.WriteLine("Type in the length: ");

int n = Convert.ToInt32(Console.ReadLine());

int[] array = ArrayGenerator.GenerateSequential(n, start: 1, capacity: 99);

array.Print(n);

Console.WriteLine("Type in position to insert to: ");

int pos = Convert.ToInt32(Console.ReadLine());

if (pos < 0 || pos >= n + 1)
{
    Console.WriteLine("Position out of range");
    return;
}

Console.WriteLine("Type in value to insert at position(pos): ");

int value = Convert.ToInt32(Console.ReadLine());

// Insert happens here
n++;

for (int i = n - 1; i >= pos; i--)
{
    array[i + 1] = array[i];
}

array[pos] = value;

Console.WriteLine("Array after insert");
array.Print(n);

