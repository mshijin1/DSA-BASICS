package Arrays;

class Student{
    public int roll_no;
    public String name;

    Student(int roll_no, String name)
    {
        this.roll_no=roll_no;
        this.name=name;
    }
}
public class arrayOfObjects {
    public static void main(String args[])
    {
        // Declaring the array of students and allocating the memory
        Student[] arr=new Student[6];
        
        arr[0]=new Student(1, "Shijin");
        arr[1]=new Student(2, "prachi");
        arr[2]=new Student(3, "rahul");
        arr[3]=new Student(4, "devansh");
        arr[4]=new Student(5, "shreyash");
        arr[5]=new Student(6, "akash");

        // Accessing elemenyts of the specified array
        for(int i=0; i<arr.length; i++)
        {
            System.out.println(" Element at " + i + "->" + " Roll no " + arr[i].roll_no + " and Name " + arr[i].name);
        }
    }
}