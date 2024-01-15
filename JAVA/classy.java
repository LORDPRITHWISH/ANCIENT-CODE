public class classy extends superman {
    classy(int x)
    {
        super(x);
    }
    public static void main(String[] args) {
        superman ob = new superman(10);
        classy obj = new classy(25);
        ob.eat();
        System.out.println("\n\n\n\n\n\n\n\n\n\n");
        obj.eat();
    }
}
