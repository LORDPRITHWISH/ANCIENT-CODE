#include <stdio.h>
#include <math.h>

int main()
{
    long long int i,s;
    int c=20;
    for (i = 0; i < c; i++)
    {
        s=pow(10,i);
        printf("\n%d\t%lld",i,s);

    }
}

