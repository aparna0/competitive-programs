#include<iostream>
#include<tuple>
using namespace std;
int main(){
    tuple<int,char,string> t,t2;
    t = make_tuple(1,'a',"aparna");

    cout<<get<0>(t)<<endl;

    get<2>(t) = "appi";

    cout<<get<2>(t)<<endl;

    cout<<"size of tuple t is "<<tuple_size<decltype(t)>::value<<endl;

    t.swap(t2);

    int i;
    char ch;
    string str;

    tie(i,ch,str) = t2;

    cout<<i<<'\t'<<ch<<'\t'<<str<<endl;

    return 0;
}
