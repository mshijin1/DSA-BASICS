package Arrays;

public class updateElement {
    public static void update(int[] arr, int element, int index)
    {
        System.out.println("Original array");
        for(int i=0; i<arr.length; i++)
        {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
        // Update the element
        arr[index]=element;
        System.out.println("Updated array");
        for(int i=0; i<arr.length; i++)
        {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }
    public static void main(String args[])
    {
        int element=3;
        int index=2;
        int[] arr={1,2,4,4,5,6,7,8,9};
        update(arr, element, index);
    }
}
