package collection_framework;
import java.util.*;

public class accessing {
    public static void main(String args[])
    {
        List<String> fruits=new ArrayList<>();
        fruits.add("apple");
        fruits.add("banana");
        fruits.add("mango");

        String first_fruit = fruits.get(0);
        System.out.println(" Element at index 0: " + first_fruit);
    }
}
