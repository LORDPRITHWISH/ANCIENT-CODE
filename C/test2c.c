#include<stdio.h>
void swap(int *a,int *b)
{
    int c;
    c=*a;
    *a=*b;
    *b=c;
}

int main()
{
    int a=10,b=20;
    printf("%d\t%d\n",a,b);
    swap(&a,&b);
    printf("%d\t%d\n",a,b);
}