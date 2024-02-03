namespace Array.Rotation.Juggling;

class Program
{
    // Function to get gcd of a and b
    static int gcd(int a, int b)
    {
        if (b == 0)
            return a;
        else
            return gcd(b, a % b);
    }

    // Function to left rotate arr[] of size n by d
    static void leftRotate(int[] arr, int d, int n)
    {
        // To handle if d >= n
        d = d % n;
        int g_c_d = gcd(d, n);
        for (int i = 0; i < g_c_d; i++)
        {
            // move i-th values of blocks
            int temp = arr[i];
            int j = i;

            while (true)
            {
                int k = j + d;
                if (k >= n)
                    k = k - n;

                if (k == i)
                    break;

                arr[j] = arr[k];
                j = k;
            }
            arr[j] = temp;
        }
    }

    // Function to print an array
    static void printArray(int[] arr, int size)
    {
        for (int i = 0; i < size; i++)
            Console.Write(arr[i] + " ");
    }

    // Driver's code
    static public void Main(string[] args)
    {
        int[] arr = { 1, 2, 3, 4, 5, 6 };
        int n = arr.Length;
        int d = 2;
        printArray(arr, n);
        Console.WriteLine();
        // Function calling
        leftRotate(arr, d, n);
        printArray(arr, n);
    }
}
