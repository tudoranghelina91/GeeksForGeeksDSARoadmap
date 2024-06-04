// C# program to rearrange the elements
// in the array such that even positioned are
// greater than odd positioned elements
using System;

internal class GFG
{
    // function to rearrange the elements in array such that
    // even positioned are greater than odd positioned
    // elements
    private static void Rearrange(int[] arr, int N)
    {
        for (int i = 0; i < N; i += 2)
        {
            // Compare it with the previous element
            if (i > 0 && arr[i - 1] > arr[i])
            {
                int temp = arr[i - 1];
                arr[i - 1] = arr[i];
                arr[i] = temp;
            }

            // Compare it with the next element
            if (i < N - 1 && arr[i + 1] > arr[i])
            {
                int temp = arr[i + 1];
                arr[i + 1] = arr[i];
                arr[i] = temp;
            }
        }
    }

    private static void Main()
    {
        // Sample Input
        int N = 4;
        int[] arr = { 1, 2, 2, 1 };

        Rearrange(arr, N);

        for (int i = 0; i < N; i++)
            Console.Write(arr[i] + " ");
        Console.WriteLine();
    }
}

// This code is contributed by shivanisinghss2110