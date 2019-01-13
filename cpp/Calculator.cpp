#include<iostream.h>
#include<conio.h>
void main()
{
clrscr();
int x;
float e,v,k;
cout<<"====Simple Calculator====\n";
cout<<"1)ADD\n2)SUB\n3)MUL\n4)DIV\nEnter your choice:";
cin>>x;

switch (x)
{
case 1:
cout<<"enter any two numbers\n";
cin>>e>>v;
cout<<"sum="<<e+v;
break;

case 2:
cout<<"enter any two numbers\n";
cin>>e>>v;
cout<<"difference=\n"<<e-v;
break;

case 3:
cout<<"enter any two numbers\n";
cin>>e>>v;
cout<<"product=\n"<<e*v;
break;

case 4:
cout<<"enter any two numbers\n";
cin>>e>>v;
cout<<"quotient="<<e/v;
cout<<"    \n";
cout<<"     \n";
break;

default:
cout<<"invalid choice\n";

}
getch ();
}
