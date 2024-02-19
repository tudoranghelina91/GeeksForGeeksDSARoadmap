using Array.Utils;

var arr = ArrayGenerator.GenerateRandom(20);
arr.Print();

for (int i = 1; i < arr.Length; i++)
{
    int j = i;
    
    while (j > 0 && arr[j] < arr[j - 1])
    {
        arr[j] += arr[j - 1];
        arr[j - 1] = arr[j] - arr[j - 1];
        arr[j] -= arr[j - 1];

        j--;
    }
}

arr.Print();