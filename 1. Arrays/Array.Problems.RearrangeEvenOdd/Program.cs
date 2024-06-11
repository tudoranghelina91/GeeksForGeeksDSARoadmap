// Skip odd

//int[] arr = { 2, 1, 2, 1 };

int[] arr = { 2, 1, 2, 1 };

for (int i = 0; i < arr.Length; i += 2)
{
    // look behind
    if (i > 0 && arr[i - 1] > arr[i])
    {
        arr[i - 1] += arr[i];
        arr[i] = arr[i - 1] - arr[i];
        arr[i - 1] -= arr[i];
    }

    // look ahead
    if (i < arr.Length - 1 && arr[i + 1] > arr[i])
    {
        arr[i] += arr[i + 1];
        arr[i + 1] = arr[i] - arr[i + 1];
        arr[i] -= arr[i + 1];
    }
}

for (int i = 0; i < arr.Length; i++)
    Console.Write(arr[i] + " ");

Console.WriteLine();