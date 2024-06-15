//Input:
//arr[] = { 2, 4, 6, 8, 9, 1, 3, 7, 5 }
//Output: 2 4 6 8 9 1 3 7 5

//Input:
//arr[] = { 1, 3, 2, 4, 7, 6, 9, 10 }
//Output: 2 4 6 10 7 1 9 3

//int[] arr = { 7, 2, 9, 4, 6, 1, 3, 8, 5 };

// also it keeps it in the same order

//int[] arr = { 2, 4, 6, 8, 9, 1, 3, 7, 5 }

int[] arr = { 7, 2, 9, 4, 6, 1, 3, 8, 5 };

int i = -1;
int j = 0;

while (j < arr.Length)
{
    if (arr[j] % 2 == 0)
    {
        i++;
        arr[j] += arr[i];
        arr[i] = arr[j] - arr[i];
        arr[j] -= arr[i];
    }

    j++;
}

for (int k = 0; k < arr.Length; k++)
{
    Console.Write(arr[k] + " ");
}