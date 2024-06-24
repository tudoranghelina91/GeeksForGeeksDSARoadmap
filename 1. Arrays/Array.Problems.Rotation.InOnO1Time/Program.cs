static void LeftRotate(int[] arr, int n, int k)
{
    // get starting point of rotated array
    int mod = k % n;

    for (int i = 0; i < n; i++)
    {
        Console.Write(arr[(i + mod) % n] + " ");
    }

    Console.WriteLine();
}

int[] arr = { 1, 3, 5, 7, 9 };
int n = arr.Length;

int k = 2;
LeftRotate(arr, n, k);

k = 3;
LeftRotate(arr, n, k);

k = 4;
LeftRotate(arr, n, k);