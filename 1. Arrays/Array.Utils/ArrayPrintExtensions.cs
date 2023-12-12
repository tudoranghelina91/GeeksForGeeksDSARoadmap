namespace Array.Utils;

public static class ArrayPrintExtensions
{
    public static void Print(this int[] arr)
    {
        Console.WriteLine("Elements in array: ");

        for (int i = 0; i < arr.Length; i++)
        {
            Console.Write(arr[i]);
            if (i < arr.Length - 1)
            {
                Console.Write(", ");
            }
        }

        Console.WriteLine();
    }

    public static void Print(this int[] arr, int n)
    {
        if (n < 0 || n >= arr.Length)
        {
            throw new ArgumentOutOfRangeException(nameof(n));
        }
        Console.WriteLine("Elements in array: ");

        for (int i = 0; i < n; i++)
        {
            Console.Write(arr[i]);
            if (i < n - 1)
            {
                Console.Write(", ");
            }
        }

        Console.WriteLine();
    }
}
