using Array.Utils;

var arr = ArrayGenerator.GenerateRandom(30);
arr.Print();

MergeSort(arr);

arr.Print();

void MergeSort(int[] arr)
{
    if (arr.Length == 1)
    {
        return;
    }

    Split(arr, out int[] arr1, out int[] arr2);

    MergeSort(arr1);
    MergeSort(arr2);

    Merge(arr, arr1, arr2);
}

void Split(int[] arr, out int[] arr1, out int[] arr2)
{
    int n = arr.Length / 2;
    int m = arr.Length / 2 + arr.Length % 2;

    arr1 = new int[n];
    arr2 = new int[m];

    int k = 0;

    for (int i = 0; i < n; i++)
    {
        arr1[i] = arr[k++];
    }

    for (int j = 0; j < m; j++)
    {
        arr2[j] = arr[k++];
    }
}

void Merge(int[] arr, int[] arr1, int[] arr2)
{
    int k = 0;

    int ii = 0, jj = 0;

    int n = arr1.Length;
    int m = arr2.Length;

    while (ii < n && jj < m)
    {
        if (arr1[ii] <= arr2[jj])
        {
            arr[k++] = arr1[ii++];
            continue;
        }

        arr[k++] = arr2[jj++];
    }

    while (ii < n)
    {
        arr[k++] = arr1[ii++];
    }

    while (jj < m)
    {
        arr[k++] = arr2[jj++];
    }
}