#include <iostream>


// #include<iomanip>
#define ohmy 1937<<
#define my 1937
#define print std::cout<<


void test1()
{
        auto a=10;
    std::cout << a<<"\n";
    auto b="prithwish";
    std::cout << b;
}

void test2()
{
    auto a="darkness ";
    int b=100;
    // std::cout<<std::setw(19)<<"lol"<<std::setw(16)<<"prithwish"<<std::setw(19)<<"lol\n";
    // std::cout<<std::setw(30)<<"lol"<<b<<"prithwish"<<a<<"lol\n";

}

void test3()
{
    std::cout<<"it is my" << my <<"\n";
    print ohmy my;

}

void test4()
{
    long double a=1.55;
    double b=5.7;
    float c=11.15141;
    std::cout<<a<<"\n"<<b<<"\n"<<c<<"\n";
}

void test5()
{
    double a=100.54;
    int i=(int)a;
    int x=static_cast<int>(a);
    std::cout<<x<<"\n";
    int iv =1500000000;
    iv=((double)iv*10)/10;
    std::cout<<iv;
}

void test()
{
    int a=10;
    double x=(double)a;
    x+=0.14125;
    std::cout<<x;
}

int main()
{
    test();  

}