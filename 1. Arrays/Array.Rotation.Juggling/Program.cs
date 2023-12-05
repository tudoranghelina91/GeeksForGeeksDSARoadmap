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

// 2.1. Go through each subset
for (int i = 0; i < arr.Length - gcd; i += gcd)
{
    // 2.2. Mark subset start as current position
    int subsetStart = i;

    // 2.3. Mark subset end as current position + gcd (offset)
    int subsetEnd = i + gcd;

    int currentPosInSubset = subsetStart;

    // 2.4. rotate the actual subset
    while (currentPosInSubset < subsetEnd)
    {
        // 2.5. Do the swapping here TODO: refine this
        arr[currentPosInSubset] += arr[currentPosInSubset + gcd];
        arr[currentPosInSubset + gcd] = arr[currentPosInSubset] - arr[currentPosInSubset + gcd];
        arr[currentPosInSubset] -= arr[currentPosInSubset + gcd];

        // 2.4.1. Move through each element of the subset to perform rotation
        currentPosInSubset += gcd;
    }
}

while (true)
{
    //int subsetStart = 0;
    //int subsetEnd = 0;
    //int step = gcd;
}