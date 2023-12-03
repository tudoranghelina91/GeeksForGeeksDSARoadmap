using Array.Utils;

int[] arr = ArrayGenerator.GenerateRandom();
arr.Print();

Console.WriteLine("Input the desired rotations to be performed on the array:");

int numberOfRotations = Math.Abs(Convert.ToInt32(Console.ReadLine()) - arr.Length);

int[] temp =  new int[arr.Length];

int k = 0;

for (int i = numberOfRotations; i < arr.Length; i++)
{
    temp[k++] = arr[i];
}

for (int i = 0; i < numberOfRotations; i++)
{
    temp[k++] = arr[i];
}

temp.Print();