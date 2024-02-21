using Array.Utils;

void MergeSort(int[] arr, int start, int end)
{
    int mid = (start + end) / 2 + (start + end) % 2;
    
    MergeSort(arr, start, mid);
    MergeSort(arr, mid, end);

    int i = start;
    int j = mid;
    int k = 0;

    // TODO:

    // 1. Copy data to temp arrays

    // 2. Merge the two halves in sorted order
}

var arr = ArrayGenerator.GenerateRandom(10);
arr.Print();

MergeSort(arr, 0, arr.Length);

arr.Print();