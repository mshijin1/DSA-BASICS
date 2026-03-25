package collection_framework;
import java.util.*;
public class object_creation {
    public static void main(String args[])
    {
        //Creating an collection of string type using arrayList implementation
        Collection<String> fruits = new ArrayList<>(); 

        //Adding elements to the collection
        fruits.add("apple");
        fruits.add("banana");
        fruits.add("mango");

        // Displaying the collection
        System.out.println("Collection: " + fruits);
    }
    
}
