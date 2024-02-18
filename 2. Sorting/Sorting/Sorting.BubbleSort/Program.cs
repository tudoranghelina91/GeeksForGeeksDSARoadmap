// See https://aka.ms/new-console-template for more information
using Array.Utils;

var arr = ArrayGenerator.GenerateRandom(20);
arr.Print();

bool sorted;

do
{
    sorted = true;
    for (int i = 0; i < arr.Length - 1; i++)
    {
        if (arr[i] > arr[i + 1])
        {
            sorted = false;
            arr[i] += arr[i + 1];
            arr[i + 1] = arr[i] - arr[i + 1];
            arr[i] -= arr[i + 1];
        }
    }
} while (!sorted);

arr.Print();