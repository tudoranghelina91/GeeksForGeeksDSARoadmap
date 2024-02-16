namespace Array.Utils;

using System;

public class ArrayGenerator
{
    public static int[] GenerateRandom(int numberOfElements = 10, int min = 1, int max = 10, bool sorted = false)
    {
        int[] arr = new int[numberOfElements];

        for (int i = 0; i < arr.Length; i++)
        {
            arr[i] = Random.Shared.Next(min, max);
        }

        if (sorted)
        {
            Array.Sort(arr);
        }

        return arr;
    }

    public static int[] GenerateSequential(int numberOfElements = 10, int start = 1, int step = 1)
    {
        int[] arr = new int[numberOfElements];

        int k = start;

        for (int i = 0; i < numberOfElements; i++)
        {
            arr[i] = k;
            k += step;
        }

        return arr;
    }

    public static int[] GenerateSequential(int numberOfElements = 10, int start = 1, int capacity = 10, int step = 1)
    {
        if (numberOfElements < 0 || numberOfElements > capacity)
        {
            throw new ArgumentOutOfRangeException(nameof(numberOfElements));
        }

        int[] arr = new int[capacity];

        int k = start;

        for (int i = 0; i < numberOfElements; i++)
        {
            arr[i] = k;
            k += step;
        }

        return arr;
    }
}