#include <iostream>
#include "initial.h"
int main()
{    
    // racer first(200,15,50,2,"formula 1","dreamcar");
    racer shower[]={racer(200,15,50,20,"formula 111","dreamcar"),
                    racer(400,25,150,12,"rusher 222","dreamcar"),
                    racer(100,35,100,42,"zappy 333","dreamcar")};
    for(racer x:shower)
    {
        x.spec();

        for(int i=0;i<x.looper();i++)
            x.speedup();
        x.spec();
    }
    // first.spec();
    // for (int i = 0; i < 10; i++)
    //     first.speedup();
    // first.spec();
    return 0;
}