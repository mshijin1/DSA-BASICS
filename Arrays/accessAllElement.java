public class accessAllElement {
    public static void listElements(int[] arr)
    {
        System.out.println("Elements");
        for(int i=0; i<arr.length; i++)
        {
            System.out.println(arr[i] + " ");
        }
    }
    public static void main(String args[])
    {
        int[] arr = {1,2,3,4,5};
        listElements(arr);
    }
    
}
