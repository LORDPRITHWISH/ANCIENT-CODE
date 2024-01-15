class test
{
    public static void main(String[] args)
    {
        int i;
        i=1;
        // for(i=0;i<5;i++)
        // {
        //     System.out.println("HELLOW!");
        //     i+=2;
        // }
        i+= i++ + ++i + ++i - ++i * --i;
        System.out.println(i);
    }
}