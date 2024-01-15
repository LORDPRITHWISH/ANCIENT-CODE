#include<iostream>

class link
{
    public:
    int a=999;
    link *nxt = NULL;

};

link* create()
{
    link *cu,*st= new  link();
    cu=st;

    for(int i=0;i<10;i++)
    {
        cu->a=100+i;
        cu->nxt=new link();
        cu = cu->nxt;
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

}

void run()
{
    link *st = create();
    print(st);
}

int main()
{
    run();
    return 0;
}