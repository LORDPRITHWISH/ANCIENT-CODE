class speed_test_java
{
    public static void main(String[] args) 
    {
        long s=0,c=1000000000;
        int i,d=0;   
        for (i=0;i<c;i++)
        {
            s+=i;
            if(i%(c/100)==0)
                System.out.println(i/(c/100));
        }
        System.out.println("\n\nTHE REASULT IS "+ s);
        
    while (s>0)
    {
        d++;
        s/=10;
    }
    System.out.println("\n\nThe digits are "+ d);
    }
}
