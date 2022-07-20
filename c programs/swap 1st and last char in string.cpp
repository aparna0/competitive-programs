#include<iostream>
#include<string.h>
using namespace std;
int main(){
    char str[50];
    cin>>str;
    int n = strlen(str);
    if(str[0] != str[n-1]){
        char t = str[0];
        str[0] = str[n-1];
        str[n-1] = t;
    }
    cout<<str;
    return 0;
}
