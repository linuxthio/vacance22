#include <iostream>
using namespace std;

void somme(int a,int b)
{
	int r=a+b;
	cout<<"la somme  de "<<a<<" + "<<b<<" = "<<r<<endl; 
}


int main()
{
	std::cout<<"je suis la "<<std::endl;
	somme(9,8);
	return 0;
}
