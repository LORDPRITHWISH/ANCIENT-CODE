#include<stdio.h>
void test1()
{
    int a=10;
    printf("%d\n",a);
    a++;
    printf("%d\n",a);
    a++;
    printf("%d\n",a);
    a++;
    printf("%d\n",a);
    a++;
    printf("%d\n",a);
}

void test2()
{
    int a=10,z=99;
    int* b=&a,*r=&z;
    int** c=&b,**d=&r;
    printf("%d",**c);

}

void test3()
{
    int a[]={11,22,33,44,55,66,77,88,99};
    int *ap=a;
    int **bp=&ap;
    printf("%d",**bp);
}
void test4()
{
    int a=10;
    int *b=&a;
    printf("%d",*b);
}

int test5()
{
    static int a=0;
    a++;
    return a;
}

void testori()
{
    int a=1;
    a+=(a+=3,5,a);
    printf("%d",a);
}

int test()
{
    int a=3;
    // a+=(1,9,3,7);
    // a+=7,2,3;
    a+=(a+=5,a);
    printf("%d",a);
}

int main()
{
    // testori();
    test();
}
