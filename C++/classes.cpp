#include<iostream>
#include<cmath>

class car
{
    private:
    std::string maker="DARKFACTORY",type,model;
    int maxspeed,speed=0,brake;
    double accelaration;
    
    public:

    car(std::string mn,std::string t,int ms=200,double ac=7.89,int b=30)
    {
        type=t;model=mn;maxspeed=ms;accelaration=ac;brake=b;
    }
    
    void speedup()
    {
        if (speed<maxspeed)
        {
            speed+=round(accelaration);
            if (speed>maxspeed)
                speed=maxspeed;
        }
        else 
            std::cout<<"MAX SPEED!\n";
            
        
    }

    void braking()
    {
        if (speed>0)
        {
            speed-=brake;
            if (speed<0)
                speed=0;
        }
        else 
            std::cout<<"WE ARE NOT MOVING\n";
    }

    void specs()
    {
        std::cout<<"\nmaker :  "<<maker<<"\nmodel :  "<<model<<"\ntype :  "<<type<<"\nmaxspeed :  "<<
        maxspeed<<"\naccelaration :  "<<accelaration<<"\nbraking :  "<<brake<<std::endl;

    }

    void speedshow()
    {
        std::cout<<"your speed is -> "<<speed<<std::endl;
    }
};

int main()
{
    // car mycar("SPEEDSTER","electric",300,8.1,40);
    car mycar("SPEEDSTER","electric");

    mycar.specs();
    
    bool runing=true;
    int ch;
    std::cout<<"\n\n\nenter choice\n 1 acelarate \n 2 decelarate\n 3 show speed\n 0 EXIT \n";
    while(runing)
    {
        std::cout<<"->";
        std::cin>>ch;
        switch (ch)
        {
        case 1:
            mycar.speedup();
            break;
        case 2:
            mycar.braking();
            break;
        case 3:
            mycar.speedshow();
            break;
        case 0:
            runing = false;
            break;
        
        default:
            std::cout<<"WTF !\
            \n you had only 4 choices and you could not even make a proper choice\n";
            break;
        }
    }

}