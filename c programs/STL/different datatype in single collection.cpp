#include<iostream>
#include<vector>
#include<variant>
#include<string>

using namespace std;
union mytype{
    int i;
    string s;
    float f;
};
int main(){
    //variant<int,string,float> type;

    vector<mytype> collection;

    return 0;
}
