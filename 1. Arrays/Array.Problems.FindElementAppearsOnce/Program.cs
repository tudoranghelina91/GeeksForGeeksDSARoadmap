int[] arr = { 2, 3, 5, 4, 5, 3, 4 };

Dictionary<int, int> map = new();

foreach (var elem in arr)
{
    if (!map.ContainsKey(elem))
    {
        map.Add(elem, 0);
    }

    map[elem]++;
}

foreach (var elem in map)
{
    if (elem.Value == 1)
    {
        Console.WriteLine(elem.Key);
        return;
    }
}