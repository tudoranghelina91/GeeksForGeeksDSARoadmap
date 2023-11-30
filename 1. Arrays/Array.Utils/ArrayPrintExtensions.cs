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
}
