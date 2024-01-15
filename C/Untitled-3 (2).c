#include<stdio.h>

int main()
{
    int a=10,b=30;
   
    a=a+b;
    b=a-b;
    a=a-b;
    printf("the number is :%d %d",a,b);
    return 0;
}