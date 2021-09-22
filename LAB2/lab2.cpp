#include  <iostream>
#include  <fstream>
#include  <string>

using   namespace  std;

int main(){
	ifstream fin("C:\Users\65660\Desktop\ee308Èí¼þ¹¤³Ì\lab2\lab2_test.cpp");
	string  s;
	while (getline(fin, s))
	{
		cout <<  s << endl;
	}
} 
