#include<iostream>

void change(int& a)
{
    a+=10;
    std::cout<<a<<std::endl;
}

int main()
{
    int pri=0;
    for(int i=0;i<10;i++)
       change(pri);
}
