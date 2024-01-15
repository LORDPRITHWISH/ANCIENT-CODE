#include <iostream>

int main()
{
    long long int i,s=0,c=1000000000;
    int d=0;
    for (i = 0; i < c; i++)
    {
        s+=i;
        if(i%(c/100)==0)
            std::cout<<i/(c/100)<<std::endl;
    }
    std::cout<<"\n\nTHE REASULT IS "<<s;

    while (s>0)
    {
        d++;
        s/=10;
    }
    std::cout<<"\n\nThe digits are "<<d;
    return 0;
}