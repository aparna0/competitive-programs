#include<iostream>
#include<map>
#include<algorithm>
using namespace std;
int main(){
    int n, x;
    cin>>n;
    map<int,int> m;

    for(int i=0; i<n; i++){
        cin>>x;
        if( m.find(x) == m.end()){
            m[x] = 1;
        }
        else{
            m[x] += 1;
        }
    }

    for(auto i : m){
        cout<<"\n"<<i.first<<" occurs "<<i.second<<" times";
    }
    return 0;
}
