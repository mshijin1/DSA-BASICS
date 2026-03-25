package Strings;

class Solution{
    public void access(String s)
    {
        System.out.println("Character of the String");
        for(int i=0; i<s.length(); i++)
        {
           System.out.print(s.charAt(i) + " "); 
        }
    }
}
public class accessElements {
    public static void main(String args[])
    {
        String name="Arundati";
        Solution obj=new Solution();

        obj.access(name);
    }
    
}
