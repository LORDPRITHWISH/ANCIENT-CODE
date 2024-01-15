fn main()
{
    let mut j=0;

    let k=10;
    let st=" it is ";
    for i in (1..k).step_by(2)
    {
        println!("{}{}{}",i,st,j);
        j+=1;
        // i+=1;
    }
}