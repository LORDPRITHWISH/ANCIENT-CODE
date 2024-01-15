#include<stdio.h>

int main() {
int arr[2][3];
int *ptr=*arr;
int *i=ptr;
printf("enter array elemnt");

for(i;i<(ptr+25);i++){
    scanf("%d",i);
}
// ptr=&arr[0][0];// resetting the pointer to start the array
i=ptr;
for(i;i<(ptr+25);i++){
    printf("%d ",*i);
}
return 0;
}