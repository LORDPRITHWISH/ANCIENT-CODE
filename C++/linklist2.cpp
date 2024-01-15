#include<iostream>
#include<math.h>
struct segment
{
    long long int val=9782;
    segment *nxt=NULL;
};

void del(segment *cur)
{
    segment *temp;
    while (cur!= NULL)
    {
 
        temp=cur;
        cur=cur->nxt;
        delete temp ;
    }
    
}

void rem(segment *cur,long long int num)
{
    segment *temp;
    long long int i=0;
    while (cur!= NULL)
    {
        i++;
        if(i==num)
        {
            temp->nxt=cur->nxt;
            delete cur;
            return;
        }
        temp=cur;
        cur=cur->nxt;
    }
    
}


void print(segment *cur)
{
    while (cur!= NULL)
    {
        std::cout<<cur->val<<'\n';
        cur=cur->nxt;
    }
    
}

void sqr(segment *cur)
{
    while (cur!= NULL)
    {
        cur->val=(int)pow(cur->val,2);
        cur=cur->nxt;
    }
    
}

segment* form(long long int size=10)
{
    long long int i=0;
    // size=(int)pow(2,30);
    segment *start,*cur;
    start = new segment();
    cur=start;
    while (true)
    {
        cur->val=i;
        if(i==size)
        break;
        i++;
        cur->nxt=new segment();
        cur=cur->nxt;
    }
    return start;
}

void work()
{
    segment *start= form(1500000);
    
    
    // sqr(start);
    rem(start,4);
    print(start);
    del(start);
    // print(start);
}


int main()
{
    work();
    return 0;
}