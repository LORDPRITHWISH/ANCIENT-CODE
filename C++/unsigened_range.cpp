#include <iostream>
int main()
{
    bool run = true;
    int a=0;
    unsigned int b=0;
    long long int pa=0,pb=0;
    std::cout<<"STARTED\n";
    while(run)
    {
        if( pa>a )
            run = false ;
        else
            pa=a;
        a++;
    }
    std::cout<<"yo\n";
    
    run = true;
    while(run)
    {
        if(pb>b )
            run = false ;
        else
            pb=b;
        b++;
    }
    std::cout<<"\na= "<<pa<<"\nb= "<<pb;
}