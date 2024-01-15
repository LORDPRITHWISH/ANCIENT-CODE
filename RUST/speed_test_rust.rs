fn main() 
{
    let mut s:i128=0;
    let mut d=0;
    // let c=1_000_000_000;
    // let c=1_000;
    let c=1000000000;

    for  i in 1..c {
        s+=i;
        if i%(c/100)==0{
            println!("{}", i/(c/100));
        }
    }
    println!("\n\nTHE REASULT IS {}", s);

    while s>0 {
        d+=1;
        s/=10;
    }
    println!("\n\nThe digits are {}", d);

}