fn main()
{
    hello("RYAN",&5,&123.5,true);
}
fn hello(x:&str,n:&i128,d:&f64,c:bool)
{
    if c
    {

        print!("{} ",d);
    }
    for _ in 1..*n
        {
            println!("HELLO {}",x);
        }

}