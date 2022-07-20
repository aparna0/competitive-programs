#include<iostream>
#include<unordered_map>
#include<utility>
#include<algorithm>
//internally it implemented as hashing
//it is not sorted,therefore it take O(n) time
using namespace std;
int main(){
    unordered_map<char,int> m1, m2;
    m1['a'] = 1;
    m1['b'] = 2;

    for(auto i : m1){
        cout<<i.first<<'\t'<<i.second<<endl;
    }

    string in = "aparna";
    for(auto i : in){
        m2[i]++;
    }

    cout<<"char\tcount\n";
    for(auto i : m2){
        cout<<i.first<<'\t'<<i.second<<endl;
    }



    return 0;
}
