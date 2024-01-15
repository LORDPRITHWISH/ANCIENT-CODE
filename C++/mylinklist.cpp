#include<iostream>
struct segment
{
    long long int val=9782;
    segment *nxt=NULL;
};

void print(segment *cur)
{
    while (cur!= NULL)
    {
        std::cout<<cur->val<<'\n';
        cur=cur->nxt;
    }
    
}

void work()
{
    
    long long int i=0,size=100;
    size=(int)pow(2,30);
    segment *start,*cur;
    start = new segment();
    cur=start;
    while (true)
    {
        cur->val=i;
        if(i>size)
        break;
        i++;
        cur->nxt=new segment();
        cur=cur->nxt;
    }
    
    cur->nxt=NULL;
    print(start);
}


int main()
{
    work();
    return 0;
}