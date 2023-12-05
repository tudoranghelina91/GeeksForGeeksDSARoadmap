using Array.Utils;

int[] arr = ArrayGenerator.GenerateSequential(10, 6);

Console.WriteLine("Elements before rotating");
arr.Print();

Console.WriteLine("Input number of rotations to be performed:");
int d = Convert.ToInt32(Console.ReadLine());

// 1. Calculate Greatest Common Divisor between the length of the input array and the number of rotations that need to be performed

int n = arr.Length;
int gcd = d;

while (gcd != 0)
{
    int r = n % gcd;
    n = gcd;
    gcd = r;
}

// 2. Rotate each subset