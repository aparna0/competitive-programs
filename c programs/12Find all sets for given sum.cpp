#include<iostream>
#include<vector>
using namespace std;

void getSet1(int, long long);
void getSet2(int, vector<int>, int);

vector<vector<int>> sets;
int main(){
    long long sum;
    cout<<"Enter sum \t";
    cin>>sum;

    getSet1(sum, 0);
    cout<<endl;

    vector<int> set(sum);
    getSet2(sum, set, 0);
    return 0;
}
void getSet1(int cs, long long res){
    if(cs == 0){
        cout<<res<<endl;
        return;
    }
    else{
        for(int i=1; i<=cs; i++){
            getSet1(cs-i,res*10+i);
        }
    }
}
void getSet2(int cs, vector<int> set, int n){
    if(cs == 0){
        for(int i=0; i<n; i++){
            cout<<set[i]<<" ";
        }
        cout<<endl;
        return;
    }
    else{
        for(int i=1; i<=cs; i++){
            set[n] = i;
            getSet2(cs-i, set, n+1);
        }
    }
}
