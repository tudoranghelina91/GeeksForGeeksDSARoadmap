// Print distinct numbers of an integer array

int[] arr = { 3, 2, 5, 8, 1, 1, 3, 2, 5, 9, 1, 7, 8 };

List<int> distinct = new();

foreach (var i in arr)
{
    if (!distinct.Contains(i))
    {
        distinct.Add(i);
    }
}

foreach (var i in distinct)
{
    Console.Write(i + " ");
}