#pragma once

#include<iostream>
class racer
{
private:
    int speed,accelaration,braking,drag;
    std::string model,brand;
public:
    racer(int sp,int ac,int br,int dr,std::string model,std::string thbrand);
    ~racer();

    void spec();

    void speedup();
};
