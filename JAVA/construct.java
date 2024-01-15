public class construct {
    public static void main(String[] args) {
        System.out.println("baller lol");
        baller ob =new baller();
        baller.eat();
        baller.main(args);
        ob.sleep();
    }
}

class baller {
    public static void main(String[] args) {
        System.out.println("boy oh boy ");
    }

    static void eat()
    {
                System.out.println("called eating ");
    }
    void sleep()
    {
                System.out.println("called sleeping");
    }
}