/*
find subsets whose sum of element is equal to given sum
*/
#include<iostream>
#include<math.h>
#include<vector>
using namespace std;

void findSubSet(int , int [], int);

int main(){
    int n;
    cout<<"enter size\t";
    cin>>n;
    int set[n];
    cout<<"\nenter "<<n<<" elements\n";
    for(int i=0; i<n; i++){
        cin>>set[i];
    }
    int m;
    cout<<"\nenter sum ";
    cin>>m;

    findSubSet(n, set, m);

    return 0;
}

void findSubSet(int no, int set[], int m){
    int e = pow(2,no) - 1;
    for(int n=0; n<=e; n++){
        int sum = 0;
        vector<int> subset;
        for(int i=log2(n); i>=0; i--){
            if(1 & (n >> i)){
                //cout<<set[i]<<" ";
                sum += set[i];
                subset.push_back(set[i]);
            }
        }
        //cout<<endl;
        if(sum == m){
            for(int i : subset){
                cout<<i<<" ";
            }
            cout<<endl;
        }
    }
}
