#include<stdio.h>
#include<limits.h>

// find maxixmum frequency character
int main() {
    int max=INT_MIN;
    char ch='\0';
    int count=0; 
    char str[]="rrmmmmmmmmmmrrrta";
    
    for(int i=0;str[i]!='\0';i++)
    { 
        for(int j=i+1;str[j]!='\0';j++)
        
            if(str[i]==str[j])
            
                count++;
        if(count>max)
        {
            max=count;
            ch=str[i];
        }
        count=0;   
        
    }
    
    printf("%c",ch);
    return 0;
}