#include <iostream>
#include <thread>
#include<math.h>

void runner()
{
    long long int s=pow(10,10),i;
    long long int a;
    std::cout<<"started to "<<s<<std::endl;
    for(i=0;i<s;i++)    
        a+=i;
    std::cout<<a<<std::endl;
    
}

int main()
{
    int thr=4,i;
    std::thread arr[thr];
    for(i=0;i<thr;i++)
    {
        arr[i]=std::thread(runner);
    }
    for(i=0;i<thr;i++)
    {
         arr[i].join();
    }
    return 0;
}