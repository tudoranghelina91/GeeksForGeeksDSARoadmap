using Array.Utils;

int[] arr = ArrayGenerator.GenerateRandom();
arr.Print();

Reverse(arr, 0, arr.Length - 1);

Console.WriteLine("Elements in array after reversing:");

arr.Print();

void Reverse(int[] array, int start, int end)
{
    if (start >= end)
    {
        return;
    }

    arr[start] += arr[end];
    arr[end] = arr[start] - arr[end];
    arr[start] -= arr[end];

    Reverse(arr, start + 1, end - 1);
}
