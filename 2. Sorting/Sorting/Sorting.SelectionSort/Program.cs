// See https://aka.ms/new-console-template for more information
using Array.Utils;

Console.WriteLine("Hello, World!");

var arr = ArrayGenerator.GenerateRandom();

arr.Print();

for (int i = 0; i < arr.Length - 1; i++)
{
    for (int j = i + 1; j < arr.Length; j++)
    {
        if (arr[i] > arr[j])
        {
            arr[i] += arr[j];
            arr[j] = arr[i] - arr[j];
            arr[i] -= arr[j];
        }
    }
}

arr.Print();