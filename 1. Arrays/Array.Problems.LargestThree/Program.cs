// See https://aka.ms/new-console-template for more information

//Input: arr[] = { 10, 4, 3, 50, 23, 90 }
//Output: 90, 50, 23

//int[] arr = { 10, 4, 3, 50, 23, 90 };

//Input: arr[] = { 6, 8, 1, 9, 2, 1, 10, 10 }
//Output: 10, 9, 10

//Input: arr[] = { 12, 13, 1, 10, 34, 1 }
//Output: 34, 13, 12
int[] arr = { 12, 13, 1, 10, 34, 1 };

int first = 0, second = 0, third = 0;

for (int i = 0; i < arr.Length; i++)
{
    if (arr[i] > first)
    {
        third = second;
        second = first;
        first = arr[i];
        continue;
    }

    if (arr[i] > second && arr[i] != first)
    {
        third = second;
        second = arr[i];
        continue;
    }

    if (arr[i] > third && arr[i] != second)
    {
        third = arr[i];
        continue;
    }
}

Console.WriteLine($"{first} {second} {third}");