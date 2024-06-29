int[] arr = { 16, 17, 4, 3, 5, 2 };

int max = 0;

for (int i = arr.Length - 1; i >= 0; i--)
{
    if (arr[i] > max)
    {
        max = arr[i];
        Console.Write(max + " ");
    }
}