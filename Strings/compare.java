package Strings;
import java.util.Scanner;
class Solution{
    public void compareStrings(String s1, String s2, Scanner sc)
    {
        if (s1.equals(s2))
        {
            System.out.println("Strings are equal");
        }
        else{
            System.out.println("Strings ar not equal");
        }
        sc.close();
    }
}
public class compare {
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);

        System.out.println("Please enter your first String");
        String s1=sc.nextLine();

        System.out.println("Please enter your second String");
        String s2=sc.nextLine();

        Solution obj=new Solution();
        obj.compareStrings(s1, s2, sc);
    }
    
}
