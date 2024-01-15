#include<stdio.h>

int main() {
int arr[3][4];
int *ptr=&arr[0][0];
int k=1;
printf("enter array elemnt  ");

for(ptr;ptr<=&arr[2][3];ptr++){
    scanf("%d",ptr);
    // *ptr=k++;
}
ptr=&arr[0][0];// resetting the pointer to start the array
for(ptr;ptr<=&arr[2][3];ptr++){
    printf("%d ",*ptr);
}
return 0;
}