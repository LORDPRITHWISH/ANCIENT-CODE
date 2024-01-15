#include<iostream>

void runner()
{
    long long int s=100000,i;
    long long int a[s];
    std::cout<<"started to "<<s<<std::endl;
    for(i=0;i<s;i++)
    {
        a[i]=i;
        if(i%(s/100)==0)
            std::cout<<i/(s/100)<<std::endl;
    }
}

int main()
{
    runner();
}