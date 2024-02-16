using Array.Utils;

var arr = ArrayGenerator.GenerateSequential(10, 5, 12, 2);

Console.WriteLine("Elements before insert");
int n = 10;
arr.Print(n);

int i = n - 1;

int key = Convert.ToInt32(Console.ReadLine());

while (i >= 0 && arr[i] > key)
{
    arr[i + 1] = arr[i];
    i--;
}

arr[i + 1] = key;
n++;

Console.WriteLine("Elements after insert");
arr.Print(n);