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

    public static int[] GenerateSequential(int numberOfElements = 10, int start = 1)
    {
        int[] arr = new int[numberOfElements];

        for (int i = 0; i < numberOfElements; i++)
        {
            arr[i] = start + i;
        }

        return arr;
    }

    public static int[] GenerateSequential(int numberOfElements = 10, int start = 1, int capacity = 10)
    {
        if (numberOfElements < 0 || numberOfElements > capacity)
        {
            throw new ArgumentOutOfRangeException(nameof(numberOfElements));
        }

        int[] arr = new int[capacity];

        for (int i = 0; i < numberOfElements; i++)
        {
            arr[i] = start + i;
        }

        return arr;
    }
}