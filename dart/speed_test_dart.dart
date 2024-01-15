void main()
{
  int c=1000000000 ,s=0,i,d=0;
  for(i=0;i<c;i++)
  {
    s+=i;
    if(i%(c/100)==0)
    {
      print("${(i/(c/100)).truncate()}",);
    }
  }
  print("\n\nTHE REASULT IS $s");

  while(s>0)
  {
    d++;
    s=s~/10;
  }
  print("\n\nThe digits are $d");
}