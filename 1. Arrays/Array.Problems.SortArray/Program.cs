// See https://aka.ms/new-console-template for more information

int Partition(int[] arr, int start, int end)
{
    int pivot = arr[end];
    int i = start - 1;

    for (int j = start; j <= end; j++)
    {
        if (arr[j] < pivot)
        {
            i++;
            Swap(arr, i, j);
        }
    }
    i++;

    Swap(arr, i, end);

    return i;
}

static void Swap(int[] arr, int i, int j)
{
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}

void QuickSort(int[] arr, int start, int end)
{
    if (end <= start)
    {
        return;
    }

    int pivot = Partition(arr, start, end);
    QuickSort(arr, start, pivot - 1);
    QuickSort(arr, pivot + 1, end);
}

int[] arr = { 10, 7, 9, 2, 8, 3, 5, 4, 6, 1 };
QuickSort(arr, 0, arr.Length - 1);

for (int i = 0; i < arr.Length; i++)
{
    Console.Write(arr[i] + " ");
}