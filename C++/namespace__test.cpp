#include<iostream>

namespace prithwish
{
    int age =19;
    std::string name="PRITHWISH";
}
namespace ronie
{
    int age =12;
    std::string name="ronie";
}

int main()
{
    std::cout<<prithwish::age<<std::endl;
    std::cout<<prithwish::name<<std::endl;
    std::cout<<ronie::age<<std::endl;
    std::cout<<ronie::name<<std::endl;

}