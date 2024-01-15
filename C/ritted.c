#include<stdio.h>
int main(){
    int i, n, arr[100], num, pos=0;
    printf("Enter the size of array : ");
    scanf("%d",&n);
    printf("Enter the elements of the array : ");
    for (i = 0; i < n; i++) {
        scanf("%d",&arr[i]);
        // arr[i]=i*10+i;
    }
    printf("Enter the element to be entered : ");
    scanf("%d",&num);

    for(i=n-1;i>=0;i--) {
        if(arr[i]<num){
            arr[i+1]=num;
            break;
        }
        arr[i+1] = arr[i];
    }

    printf("\nThe new array is : ");
    for(i=0;i<=n;i++) {
        printf("%d ", arr[i]);
    }
}
