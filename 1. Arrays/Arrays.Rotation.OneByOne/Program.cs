using Array.Utils;

int[] arr = ArrayGenerator.GenerateRandom();
arr.Print();

Console.WriteLine("Input the desired rotations to be performed on the array:");

int numberOfRotations = Convert.ToInt32(Console.ReadLine());

for (int rotation = 1; rotation <= numberOfRotations; rotation++)
{
    int carry = arr[0];

    for (int i = 1; i < arr.Length; i++)
    {
        arr[i - 1] = arr[i];
    }

    arr[arr.Length - 1] = carry;
}
Console.WriteLine("Arrat after rotation:");
arr.Print();
