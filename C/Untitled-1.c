#include<stdio.h>

int main()
{
    int a,b;
    printf("enter number\n");
    scanf("%d %d",&a,&b);
    a=a+b;
    b=a-b;
    a=a-b;
    printf("the number is :%d %d",a,b);
    return 0;
}