#include<stdio.h>
#include<math.h>
int main()
{
    int i,j,c,n=0,si=10;
    for(i=0;i<si;i++)
    {
        c=n;
        for(j=0;j<si;j++)
        {       
            printf("  %d",((int)ceil(si/2.0)-n+c));
            if (j>(si-n-2))
                c+=1;
            else if (c>0)
                c-=1;
        }
        if  (i==((si/2.0)-1));
        else if (i<(si/2))
            n+=1;
        else 
            
            n-=1;
        printf("\n");
        
    }
}