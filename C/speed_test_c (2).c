#include <stdio.h>
int main()
{
    long long int i,s=0,c=1000000000;
    int d=0;
    for (i = 0; i < c; i++)
    {
        s+=i;
        if(i%(c/100)==0)
            printf("\n%d", i/(c/100));
    }
    printf("\n\nTHE REASULT IS %lld", s);

    while (s>0)
    {
        d++;
        s/=10;
    }
    printf("\n\nThe digits are %d", d);

}