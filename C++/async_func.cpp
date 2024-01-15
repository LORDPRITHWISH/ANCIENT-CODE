#include<iostream>
#include <future>
int print(std::string x)
{
    int i=10;
    while (i)
    {
        std::cout<<"yo yo"<<x<<std::endl;
        std::this_thread::sleep_for(std::chrono::milliseconds(5));
        i--;
    }
    return x.length();
    
}

int main()
{
    std::future<int> pr1= std::async (print," ron");
    std::future<int> pr2= std::async (print," baller");
    std::cout<<pr1.get();
    std::cout<<pr2.get();

    return 0;

}