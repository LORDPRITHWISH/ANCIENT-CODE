#include<iostream>
#include<class_object_list.h>

class racer
{
private:
    int speed,accelaration,braking,drag;
    // int speed=0;
    std::string model,brand;
public:
    racer(int sp,int ac,int br,int dr,std::string model,std::string thbrand);
    // racer(int sp):speed(sp) {};
    // racer(int this.speed){};   does not work
    ~racer();

    void spec()
    {
        std::cout<<"\n"<<speed<<"\n"<<accelaration<<"\n"<<braking<<"\n"<<drag<<"\n"<<model<<"\n"<<brand<<"\n";
        // std::cout<<"\n"<<speed;
    }
};

racer::racer(int sp,int ac,int br,int dr,std::string mo,std::string ba)
{
    std::cout<<"constucting\n";
    speed=sp;accelaration=ac;braking=br;drag=dr;model=mo;brand=ba;
}

racer::~racer()
{
    std::cout<<"\nWell poop";
}


int main()
{
    racer first(200,15,50,2,"formula 1","dreamcar");
    // racer first(200);
    first.spec();
    return 0;
}