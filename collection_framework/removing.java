package collection_framework;
import java.util.*;
public class removing {
    public static void main(String args[])
    {
        Collection<String> fruits = new ArrayList<>();
        fruits.add("mango");
        fruits.add("kiwi");
        fruits.add("banana");

        System.out.println(" fruits: " + fruits);
        fruits.remove("kiwi");

        System.out.println("After removing: " + fruits);
    }
    
}
