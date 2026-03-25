package Arrays.ArrayClasses;

import java.util.Arrays;

public record asList() {
    public static void main(String args[])
    {
        int[] arr={1,2,3,4,5};

        // Convert the elements as list
        System.out.println("Interger arrays as List: " + Arrays.asList(arr));

    }
}
