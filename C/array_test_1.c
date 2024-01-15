#include<stdio.h>
void printer(int arr[][3])
{
    printf("IT IS :  %d\n",*(*(arr+2)+1));
    // *(arr+1)*=10;
}

int main()
{
    // int a[]={00,11,22,33,44,55,66,77,88,99,1100};
    int a[][3]={{11,22,33},{44,55,66},{77,88,99}};
    printer(a);
    printer(a);
    return 0;
}