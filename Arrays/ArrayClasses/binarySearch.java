package Arrays.ArrayClasses;

import java.util.Arrays;
public abstract class binarySearch {
    public static void main(String args[])
    {
        int key=94;
        int[] arr={94,75,474,84,73};
        
        Arrays.sort(arr);
        System.out.println("Original array: ");
        for(int i=0; i<arr.length; i++)
        {
            System.out.print(arr[i] + " ");
        }
        System.out.println();

        System.out.print("Element found at " + Arrays.binarySearch(arr, key));
    }
}
