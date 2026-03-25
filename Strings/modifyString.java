package Strings;

import java.util.*;

class Solution{
    public String modify(String first_name)
    {
        String sername="Murugan";
        // appending thr sername to the orignal name
        String full_name=first_name + " " + sername;

        return full_name;
    }
}

public class modifyString {
    public static void main(String args[])
    {
        String first_name="Shiiin";
        Solution obj=new Solution();

        System.out.println("original: " + first_name);
        System.out.println("After modification: " + obj.modify(first_name));

    }
    
}
