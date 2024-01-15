#include<stdio.h>
#include<string.h>
#include<iostream>
using namespace std;


void salting();

int main() {
salting();
return 0;
}

void salting(){

    char pass[]="abssba";
    int l=strlen(pass);
    char def[]="1234";
    int s=strlen(def);
    cout<<l;
    cout<<s;
   
    char newpass[l+s];

    for(int i=0;i<l/2;i++)
    {
         newpass[i]=pass[i];
    }
    strcat(newpass,def); 
     int j=(l/2)+s;
    for(int i=l/2;pass[i]!=0 && j<(l+s);i++)
    {
        newpass[j]=pass[i];
        j++;
    }
    puts(newpass);
    for(int i=0;newpass[i]!=0;i++){
        printf("%c",newpass[i]);
    }
}