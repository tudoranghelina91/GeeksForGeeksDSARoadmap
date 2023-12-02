using Array.Utils;

int[] arr = ArrayGenerator.GenerateRandom();
arr.Print();

Console.WriteLine("Input the desired rotations to be performed on the array:");

int numberOfRotations = Convert.ToInt32(Console.ReadLine());

int[] temp =  new int[arr.Length];

int k = 0;

for (int i = arr.Length - numberOfRotations; i < arr.Length; i++)
{
    temp[k++] = arr[i];
}

for (int i = 0; i < arr.Length - numberOfRotations; i++)
{
    temp[k++] = arr[i];
}

temp.Print();