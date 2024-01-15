import java. math. BigInteger;
class bigint
{
    public static void main(String[] args) {
        BigInteger a=new BigInteger("100000000000000000000000000000000000000000000000000000000000000000");
        BigInteger b=new BigInteger("5");
        System.out.println(a.add(b));
        System.out.println(a.multiply(b));
        System.out.println(a.subtract(b));
        System.out.println(a.mod(b));
        System.out.println(a.divide(b));
        System.out.println(a.pow(10));
        
    }    
}
