//Input: arr = { 4, 6, 3, 7}
//Output:
//3
//Explanation: There are three triangles
//possible {3, 4, 6}, { 4, 6, 7}
//and {3, 6, 7}.
//Note that {3, 4, 7} is not a possible triangle.

//Input: arr = { 10, 21, 22, 100, 101, 200, 300}.
//Output:
//6
//Explanation: There can be 6 possible triangles:
//{ 10, 21, 22}, { 21, 100, 101}, { 22, 100, 101},
//{ 10, 100, 101}, { 100, 101, 200}
//and {101, 200, 300}

int[] arr = { 10, 21, 22, 100, 101, 200, 300 };

Array.Sort(arr);

int numberOfTriangles = 0;

for (int i = arr.Length - 1; i >= 1; i--)
{
    int l = 0, r = i - 1;
    while (l < r)
    {
        if (arr[l] + arr[r] > arr[i])
        {
            numberOfTriangles += r - l;
            r--;
        }
        else
        {
            l++;
        }
    }
}

Console.WriteLine(numberOfTriangles);