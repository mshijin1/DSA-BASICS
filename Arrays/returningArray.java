package Arrays;

public class returningArray {
    public static int[] update(int[] arr1)
    {
        arr1[6]=8;
        arr1[5]=7;
        return arr1;
    }
    public static void main(String args[])
    {
        int[] arr1={2,3,4,5,6,6,7};

        System.out.println("Original Array");
        for(int i=0; i<arr1.length; i++)
        {
            System.out.print(arr1[i] + " ");
        }
        System.out.println();

        // Printing upadated array
        int[] arr2=update(arr1);

        System.out.println("Updated Array");
        for(int j=0; j<arr2.length; j++)
        {
            System.out.print(arr2[j] + " ");
        }

        System.out.println();
        for(int i=0; i<arr1.length; i++)
        {
            System.out.print(arr1[i] + " ");
        }
    }
}
