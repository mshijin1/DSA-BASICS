public class factorial {
    public static void main(String args[])
    {
        int n=5;
        int fact=1;
        while(n>0)
        {
            fact *=n;
            n--;
        }
        System.out.println("The factorial is: " + fact);
    }
    
}
