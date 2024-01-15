#include<thread>
#include<iostream>
void print(std::string x)
{
    int i=100;
    while (i)
    {
        std::cout<<"yo yo"<<x<<std::endl;
        std::this_thread::sleep_for(std::chrono::milliseconds(500));
        i--;
    }
    
}

int main()
{
    std::thread pr1(print," ron");
    std::thread pr2(print," baller");
    pr1.join();
    pr2.join();

}