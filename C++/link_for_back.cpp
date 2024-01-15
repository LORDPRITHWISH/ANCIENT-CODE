#include<iostream>

class link
{
    public:
    int a=999;
    link *nxt = NULL,*pre = NULL;

};

link* create()
{
    link *cu,*st= new  link();
    cu=st;
    int i=0;
    while(true)
    {
        cu->a=100+i++;
        if(i<100)
        {
            cu->nxt=new link();
            cu->nxt->pre=cu;
            cu = cu->nxt;
        }
        else 
            break;
    }
    return st;
}

void print(link *st)
{
    while(st != NULL)
    {
        std::cout<<st->a<<std::endl;
        st=st->nxt;
    }
    std::cout<<"\n\n\n";

}

void test(link *st)
{
    while(st->nxt != NULL)
        st=st->nxt;

    while(st != NULL)
    {
        std::cout<<st->a<<std::endl;
        st=st->pre;
    }

}

void run()
{
    link *st = create();
    print(st);
    test(st);
}

int main()
{
    run();
    return 0;
}
