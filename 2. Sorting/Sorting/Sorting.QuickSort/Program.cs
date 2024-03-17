using Array.Utils;

void QuickSort(int[] arr, int start, int end)
{
    if (start >= end)
    {
        return;
    }

    int pivot = end;

    int i = start - 1;

    for (int j = start; j < end; j++)
    {
        if (arr[j] < arr[pivot])
        {
            i++;
            SwapElements(arr, i, j);
        }
    }

    i++;
    SwapElements(arr, i, end);

    pivot = i;

    QuickSort(arr, start, pivot - 1);
    QuickSort(arr, pivot + 1, end);
}

static void SwapElements(int[] arr, int i, int j)
{
    if (i == j)
    {
        return;
    }

    arr[i] += arr[j];
    arr[j] = arr[i] - arr[j];
    arr[i] -= arr[j];
}

var arr = new int[] { 8, 2, 4, 7, 1, 3, 9, 6, 5 };
arr.Print();
QuickSort(arr, 0, arr.Length - 1);
arr.Print();