#include <stdio.h>
#include <string.h>

int main() {
    char pass[] = "Ritam";
 
    char newpass[5];
   
    for(int i=0;i<5;i++){
     newpass[i]=pass[i];
    }
    
    puts(newpass);
    printf("%d",strlen(newpass));
    return 0;
}