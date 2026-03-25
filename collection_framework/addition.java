package collection_framework;
import java.util.*;

public class addition {
    public static void main(String args[])
    {
        Collection<Integer> morenumbers= new ArrayList<>();
        Collection<Integer> numbers= new ArrayList<>();
        numbers.add(1);
        numbers.add(2);
        numbers.add(3);

        System.out.println("numbers: " + numbers);

        morenumbers.add(4);
        morenumbers.add(5);

        System.out.println("more numbers: " + morenumbers);

        numbers.addAll(morenumbers);
        System.out.println("Modified numbers: " + numbers);

        morenumbers.addAll(numbers);
        System.out.println("Modified morenumbers: " + morenumbers);


    }
    
}
