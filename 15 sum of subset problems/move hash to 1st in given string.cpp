#include<iostream>
using namespace std;
int main(){
    string str1;
    cin>>str1;
    int n = str1.length();
    int c=0;
    char str2[n];
    for(int i=0; i<n; i++){
        if(str1[i] == '#'){
            c++;
        }
    }
    for(int i=0; i<c; i++){
        str2[i] = '#';
    }
    for(int i=0; i<n; i++){
        if(str1[i] == '#'){
            continue;
        }
        str2[c++] = str1[i];
    }
    cout<<str2;
    return 0;
}
