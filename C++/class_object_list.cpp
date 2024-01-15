#include "class_object_list.h"

racer::racer(int sp,int ac,int br,int dr,std::string mo,std::string ba)
{
    std::cout<<"constucting\n";
    speed=sp;accelaration=ac;braking=br;drag=dr;model=mo;brand=ba;
}

racer::~racer()
{
    std::cout<<"\nWell poop";
}

void racer::spec()
{
    std::cout<<"\n"<<speed<<"\n"<<accelaration<<"\n"<<braking<<"\n"<<drag<<"\n"<<model<<"\n"<<brand<<"\n";
    }

void racer::speedup()
{
    speed+=accelaration;
}