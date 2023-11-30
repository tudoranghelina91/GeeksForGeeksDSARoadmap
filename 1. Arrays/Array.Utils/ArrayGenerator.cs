﻿namespace Array.Utils;

using System;

public class ArrayGenerator
{
    public static int[] GenerateRandom(int numberOfElements = 100, int min = 1, int max = 100, bool sorted = false)
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
}
