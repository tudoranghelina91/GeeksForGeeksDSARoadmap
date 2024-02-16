using Array.Utils;
int[] arr = ArrayGenerator.GenerateSequential(10, 5, 1);

arr.Print();

int key = Convert.ToInt32(Console.ReadLine());

int start = 0;
int end = arr.Length - 1;
int mid = (start + end) / 2;

while (start <= end)
{
    if (arr[mid] == key)
    {
        Console.WriteLine($"Element {key} found at position {mid}");
        return;
    }

    if (key < arr[mid])
    {
        end = mid - 1;
    }

    if (key > arr[mid])
    {
        start = mid + 1;
    }

    mid = (start + end) / 2;
}

Console.WriteLine($"Element {key} not found");