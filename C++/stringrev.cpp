#include<iostream>
using namespace std;

int main() {
    string str = "Prithwish";  
    char temp;
    int i = 0, j = str.length() - 1;
    while (i < j)
    {
        temp = str[i];
        str[i] = str[j];
        str[j] = temp;
        i++;
        j--;
    }
    cout << str << endl;  
    return 0;
}