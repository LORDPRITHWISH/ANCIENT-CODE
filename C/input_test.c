#include<stdio.h>

int main() {
char op;
printf("enter operator");
scanf(" %c",&op);

int a,b;
printf("enter oparand a and b");
scanf("%d %d",&a,&b);

switch(op){
    case '+':printf("%d",a+b);
             break;
    case '-':printf("%d",a-b);
              break;
    case '*':printf("%d",a*b);
             break;
    case '/': printf("%f",a/b);
            break;
    default :printf("wrong operator");
}
return 0;
}