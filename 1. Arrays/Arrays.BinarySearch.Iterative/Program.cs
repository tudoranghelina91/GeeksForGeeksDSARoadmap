using Array.Utils;

int[] arr = ArrayGenerator.GenerateRandom(sorted: true);

arr.Print();

int lo = 0;
int hi = arr.Length - 1;
int mid = (lo + hi) / 2;

Console.WriteLine("Type in a number for target: ");
int target = Convert.ToInt32(Console.ReadLine());

while (lo <= hi)
{
    if (arr[mid] == target)
    {
        Console.WriteLine($"Element {target} found at position {mid}");
        return;
    }

    if (target < arr[mid])
    {
        hi = mid - 1;
    }

    if (target > arr[mid])
    {
        lo = mid + 1;
    }

    mid = (lo + hi) / 2;
}

Console.WriteLine($"Element {target} not found");
