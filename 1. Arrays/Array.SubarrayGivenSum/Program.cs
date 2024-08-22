int[] arr = { 1, 4, 0, 0, 3, 10, 5 };
int sum = 7;

int i = 0;
int j = i + 1;
int target = arr[i] + arr[j];
bool found = false;

while (i < j && j < arr.Length)
{
    if (target < sum)
    {
        j++;
        target += arr[j];
    }

    if (target > sum)
    {
        target -= arr[i];
        i++;
    }

    if (target == sum)
    {
        found = true;
        break;
    }
}

if (!found)
{
    Console.WriteLine(-1);
    return;
}

for (int ii = i; ii <= j; ii++)
{
    Console.Write(arr[ii] + " ");
}