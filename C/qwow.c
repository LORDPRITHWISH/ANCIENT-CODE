#include<stdio.h>
int main()
{
    int a=10;
    a+=(a+=(a+=5,5),5);
    printf("%d",a);
    return 0;
    
}