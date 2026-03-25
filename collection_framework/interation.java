package collection_framework;
import java.util.*;
import java.util.concurrent.ArrayBlockingQueue;

public class interation {
    public static void main(String args[])
        {
            Collection<String> list=new ArrayList<>();
            
            list.add("Shijin");
            list.add("pranav");
            list.add("taarush");

            System.out.println("list: " + list);

            Iterator<String> it = list.iterator();

            while(it.hasNext()){
                System.out.print("elements: " + it.next() + " ");
            }
        }
}
