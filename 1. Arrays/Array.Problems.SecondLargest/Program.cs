// Promotion system approach

//Input: arr[] = { 12, 35, 1, 10, 34, 1 }
//Output: The second largest element is 34.
//Explanation: The largest element of the array is 35 and the second largest element is 34

//Input: arr[] = { 10, 5, 10 }
//Output: The second largest element is 5.
//Explanation: The largest element of the array is 10 and the second largest element is 5

//Input: arr[] = { 10, 10, 10 }
//Output: The second largest does not exist.
//Explanation: Largest element of the array is 10 there is no second largest element

int[] arr = [10, 10, 10];

int first = 0;
int second = 0;

for (int i = 0; i < arr.Length; i++)
{
    if (arr[i] > first)
    {
        second = first;
        first = arr[i];
        continue;
    }

    if (arr[i] > second && arr[i] != first)
    {
        second = arr[i];
        continue;
    }
}

Console.WriteLine(second);