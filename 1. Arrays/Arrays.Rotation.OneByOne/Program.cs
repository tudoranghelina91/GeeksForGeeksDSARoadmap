using Array.Utils;

int[] arr = ArrayGenerator.GenerateRandom();
arr.Print();

Console.WriteLine("Input the desired rotations to be performed on the array:");

int numberOfRotations = Convert.ToInt32(Console.ReadLine());

for (int rotation = 1; rotation <= numberOfRotations; rotation++)
{
    int carry = arr[arr.Length - 1];

    for (int i = arr.Length - 1; i >= 1; i--)
    {
        arr[i] = arr[i - 1];
    }

    arr[0] = carry;
}
Console.WriteLine("Arrat after rotation:");
arr.Print();
