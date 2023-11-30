// See https://aka.ms/new-console-template for more information
using Array.Utils;

Console.WriteLine("Hello, World!");

int[] arr = ArrayGenerator.GenerateRandom(5, sorted: true);

arr.Print();

int lo = 0;
int hi = arr.Length - 1;
int mid = (lo + hi) / 2;

Console.WriteLine("Type in a number for target: ");
int target = Convert.ToInt32(Console.ReadLine());

int position = Search(target, lo, hi);

if (position == - 1)
{
    Console.WriteLine($"Element {target} not found");
    return;
}

Console.WriteLine($"Element {target} found at position {position}");

int Search(int target, int lo, int hi)
{
    int mid = (lo + hi) / 2;

    if (arr[mid] == target)
    {
        return mid;
    }

    if (target < arr[mid])
    {
        return Search(target, lo, mid - 1);
    }

    if (target > arr[mid])
    {
        return Search(target, mid + 1, hi);
    }

    return -1;
}