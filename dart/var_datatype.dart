void main()
{
  var i;
  print(i);
  i=10;
  print(i);
  i=false;
  print(i);
  i="DARKLORD";
  print(i);
  i=19.24;
  print(i);
  i=9223372036854775807;
  print(i);
  i=1000000000000000000;
  print(i);
  i=BigInt.parse('100000000000000000000000000000000000');
  print(i);
  i=BigInt.from(100).pow(100);
  print(i);
}