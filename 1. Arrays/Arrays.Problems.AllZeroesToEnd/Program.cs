// See https://aka.ms/new-console-template for more information
//Move all zeroes to end of array
//Last Updated : 18 Sep, 2023
//Given an array of random numbers, Push all the zero’s of a given array to the end of the array. For example, if the given arrays is {1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0}, it should be changed to {1, 9, 8, 4, 2, 7, 6, 0, 0, 0, 0}. The order of all other elements should be same. Expected time complexity is O(n) and extra space is O(1).

//Example:

//Input: arr[] = { 1, 2, 0, 4, 3, 0, 5, 0 };
//Output: arr[] = { 1, 2, 4, 3, 5, 0, 0, 0 };

//Input: arr[]  = { 1, 2, 0, 0, 0, 3, 6 };
//Output: arr[] = { 1, 2, 3, 6, 0, 0, 0 };

//Input: arr[] = { 1, 2, 0, 0, 3, 6, 0 };

// Do it in two passes:

// 1st pass - determine loop
// 2nd pass - write zeroes at end

int[] arr = { 1, 2, 0, 0, 3, 6, 0 };

int count = 0;

for (int i = 0; i < arr.Length; i++)
{
    if (arr[i] != 0)
    {
        arr[count++] = arr[i];
    }
}

while (count < arr.Length)
{
    arr[count++] = 0;
}

//// My solution - extremely inefficient but gets the job done - O(n^3)
//bool allZeroesAtEnd;
//int end = arr.Length;

//do
//{
//    allZeroesAtEnd = true;
//    for (int i = 0; i < end; i++)
//    {
//        if (arr[i] == 0)
//        {
//            for (int j = i; j < arr.Length - 1; j++)
//            {
//                arr[j] += arr[j + 1];
//                arr[j + 1] = arr[j] - arr[j + 1];
//                arr[j] -= arr[j + 1];
//            }
//            end--;
//            allZeroesAtEnd = false;
//        }
//    }
//} while (!allZeroesAtEnd);

for (int i = 0; i < arr.Length; i++)
{
    Console.Write(arr[i] + " ");
}