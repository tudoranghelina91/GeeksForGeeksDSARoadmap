// C# program for reversal algorithm
// of array rotation
using System;

namespace Array.Problems.RotationWithReversal
{
    internal class Program
    {
        /* Function to left rotate arr[]
        of size n by d */

        private static void LeftRotate(int[] arr, int d)
        {
            if (d == 0)
                return;
            var n = arr.Length;
            // in case the rotating factor is
            // greater than array length
            d = d % n;
            ReverseArray(arr, 0, d - 1);
            ReverseArray(arr, d, n - 1);
            ReverseArray(arr, 0, n - 1);
        }

        /* Function to reverse arr[] from
        index start to end*/

        private static void ReverseArray(int[] arr, int start,
                                int end)
        {
            int temp;
            while (start < end)
            {
                temp = arr[start];
                arr[start] = arr[end];
                arr[end] = temp;
                start++;
                end--;
            }
        }

        /*UTILITY FUNCTIONS*/
        /* function to print an array */

        private static void PrintArray(int[] arr)
        {
            for (var i = 0; i < arr.Length; i++)
                Console.Write(arr[i] + " ");
        }

        // Driver code
        public static void Main()
        {
            int[] arr = { 1, 2, 3, 4, 5, 6, 7 };
            var n = arr.Length;
            var d = 2;

            LeftRotate(arr, d); // Rotate array by 2
            PrintArray(arr);
        }
    }
}

// This code is contributed by Sam007