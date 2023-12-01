using Array.Utils;

int[] arr = ArrayGenerator.GenerateRandom();
arr.Print();

int start = 0;
int end = arr.Length - 1;

while (start < end)
{
    arr[start] += arr[end];
    arr[end] = arr[start] - arr[end];
    arr[start] -= arr[end];

    start++;
    end--;
}

Console.WriteLine("Elements in array after reversing:");

arr.Print();
