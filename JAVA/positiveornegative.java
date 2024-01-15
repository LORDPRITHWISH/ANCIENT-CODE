import java.util.*;

public class positiveornegative { // positive or negative.
    public static void main(String args[]) {
        Scanner scan = new Scanner(System.in);
        System.out.print("enter number:\t");
        int number = scan.nextInt();
        if (number > 0) {
            System.out.println("its positive number");
        } else {
            System.out.println("its negative number");

        }
    }
}