#include<stdio.h>

int main() {
  char ch='A';
  char *ptr=&ch;
  printf("capital letters are :");
for(*ptr;ch<='z';ch++){
   printf("%c ",ch);
   if(ch=='a'){
    printf(" \n small letters are :");
    ch='a'-1;
  }
}
return 0;
}