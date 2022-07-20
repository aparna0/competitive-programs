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
    cout<<"\nenter divisor ";
    cin>>m;

    findSubSet(n, set, m);

    return 0;
}

void findSubSet(int n, int set[], int m){
    int e = pow(2,n) - 1;
    for(int n=0; n<=e; n++){
        int sum = 0;
        vector<int> subset;
        for(int i=log2(n); i>=0; i--){
            if(1 & (n >> i)){
                sum += set[i];
                subset.push_back(set[i]);
            }
        }
        if(sum%m == 0){
            for(int i : subset){
                cout<<i<<" ";
            }
            cout<<endl;
        }
    }
}
