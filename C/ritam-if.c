#include<stdio.h>

int main() 
{
    printf("Capital letter are :\t");
    for(char ch='A';ch<='z';ch++)
    {
        printf("%c ",ch);        
        if(ch=='Z')
        {
            printf(" \nsmall letter are:\t\t");
            ch='a'-1;
        }
    }
return 0;
}