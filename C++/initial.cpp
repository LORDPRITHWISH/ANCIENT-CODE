#include "initial.h"

racer::racer(int sp,int ac,int br,int dr,std::string mo,std::string ba)
{
    std::cout<<"constucting\n";
    speed=sp;accelaration=ac;braking=br;drag=dr;model=mo;brand=ba;
}

void racer::spec()
{
    std::cout<<"\nSPECS ARE =>\n "<<speed<<"\n "<<accelaration<<"\n "<<braking<<"\n "<<drag<<"\n "<<model<<"\n "<<brand<<"\n";
    }

void racer::speedup()
{
    speed+=accelaration;
    std::cout<<"\n"<<speed<<"\n";
}

