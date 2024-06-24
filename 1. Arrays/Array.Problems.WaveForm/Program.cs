//Examples:

//Input:
//arr[] = { 10, 5, 6, 3, 2, 20, 100, 80 }
//Output:
//arr[] = { 10, 5, 6, 2, 20, 3, 100, 80 }
//Explanation:
//here you can see {10, 5, 6, 2, 20, 3, 100, 80}
//first element is larger than the second and the same thing is repeated again and again. large element – small element-large element -small element and so on .it can be small element-larger element – small element-large element -small element too. all you need to maintain is the up-down fashion which represents a wave. there can be multiple answers.

//Input: arr[] = { 20, 10, 8, 6, 4, 2 }
//Output: arr[] = { 20, 8, 10, 4, 6, 2 }

int[] arr = { 10, 5, 6, 3, 2, 20, 100, 80 };

for (int i = 0; i < arr.Length; i += 2)
{
    if (i > 0 && arr[i] < arr[i - 1])
    {
        arr[i] += arr[i - 1];
        arr[i - 1] = arr[i] - arr[i - 1];
        arr[i] -= arr[i - 1];
    }

    if (i < arr.Length - 1 && arr[i] < arr[i + 1])
    {
        arr[i] += arr[i + 1];
        arr[i + 1] = arr[i] - arr[i + 1];
        arr[i] -= arr[i + 1];
    }
}

foreach (int num in arr)
{
    Console.Write(num + " ");
}