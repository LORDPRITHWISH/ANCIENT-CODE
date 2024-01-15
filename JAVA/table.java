import java.util.*;
public class table
{
    public static void main(String args [])
    {
        int i;
        Scanner sc=new Scanner(System.in);
        System.out.print("INPUT THE NUMBER :\t");
        int n=sc.nextInt();
        System.out.println("\n\nTHE TABLE IS:");
        for(i=1;i<=10;i++)
        System.out.println(n+" X "+i+" = "+(n*i));          
    }
    
}

    
