#include<stdio.h>
#include<string.h>

void salting();

int main() {
    salting();
    return 0;
}

void salting() {

    char pass[]="abssba";
    int l=strlen(pass);
    char def[]="1234";
    int s=strlen(def);

    char newpass[l+s];

    for(int i=0; i<l/2; i++) {
        newpass[i]=pass[i];
    }
    strcat(newpass,def);
    int j=(l/2)+s;
    for(int i=l/2; pass[i]!='\0' && j<(l+s); i++) {
        newpass[j]=pass[i];
        j++;
    }
    newpass[l+s]='\0';
    puts(newpass);
    for(int i=0; newpass[i]!='\0'; i++) {
        printf("%c",newpass[i]);
    }
}
