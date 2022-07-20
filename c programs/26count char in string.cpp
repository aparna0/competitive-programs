#include<iostream>
using namespace std;
int main(){
    string str;
    cin>>str;
    int i,j,c;
    i=0;
    while(i < str.length()){
        c = 1;
        j = i+1;
        while(str[i] == str[j] && j < str.length()){
            c++;
            j++;
        }
        cout<<str[i]<<c;
        i = j;
    }
    return 0;
}
