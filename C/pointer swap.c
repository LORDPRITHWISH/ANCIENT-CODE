#include<stdio.h>
void _swap(int *a,int *b);

int main() {
    int x=5;
    int y=10;
    _swap(&x,&y);
    printf("x:%d \n",x);
    printf("y:%d \n",y);
    return 0;
}

void _swap(int *a,int *b){
    
    int temp=*a;
    *a=*b;
    *b=temp;
    printf("a:%d \n",*a);
    printf("b:%d \n",*b);
}