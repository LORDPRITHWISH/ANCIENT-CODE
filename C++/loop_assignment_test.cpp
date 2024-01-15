#include<iostream>
int main()
{
    // int s=100,i,a[s];
    int s=10,i;
    int a[s];
    for(int j:a)
    {
        std::cout<<j<<"\t";
        j=13764;
        std::cout<<j<<"\n";
    }
    // for(i=0;i<s;i++)
    // {
    //     a[i]=13764;
    // }

    std::cout<<"\n\n\n\n\n\n";

    for(int j:a)
    {
        std::cout<<j<<std::endl;
    }

}