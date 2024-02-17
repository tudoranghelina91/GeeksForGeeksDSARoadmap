// See https://aka.ms/new-console-template for more information
using Array.Utils;

Console.WriteLine("Hello, World!");

var arr = ArrayGenerator.GenerateSequential(10, 1, 1);
int n = arr.Length;
arr.Print();

int key = Convert.ToInt32(Console.ReadLine());

int start = 0;
int end = n - 1;

int mid = (start + end) / 2;

while (start <= end)
{
    if (arr[mid] == key)
    {
        break;
    }

    if (key > arr[mid])
    {
        start = mid + 1;
    }

    if (key < arr[mid])
    {
        end = mid - 1;
    }

    mid = (start + end) / 2;
}

if (arr[mid] != key)
{
    Console.WriteLine($"No element {key} found to delete");
    return;
}
for (int i = mid; i < n - 1; i++)
{
    arr[i] = arr[i + 1];
}

n--;

arr.Print(n);

