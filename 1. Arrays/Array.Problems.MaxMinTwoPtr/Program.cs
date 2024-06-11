// See https://aka.ms/new-console-template for more information
int[] arr = { 1, 2, 3, 4, 5, 6, 7 };

// Store result in temp array

int i = 0;
int j = arr.Length - 1;
int k = 0;

int[] aux = new int[arr.Length];

while (i <= j)
{
    if (k < arr.Length)
        aux[k++] = arr[j--];

    if (k < arr.Length)
        aux[k++] = arr[i++];
}

for (int l = 0; l < aux.Length; l++)
{
    Console.Write(aux[l] + " ");
}