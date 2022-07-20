#include<iostream>
#include<math.h>
using namespace std;

void printPowerSet(int , int []);

int main(){
    int n;
    cout<<"enter size of set";
    cin>>n;
    int set[n];
    cout<<"enter "<<n<<" elements \n";
    for(int i=0; i<n; i++){
        cin>>set[i];
    }
    printPowerSet(n , set);
    return 0;
}

void printPowerSet(int n, int set[]){
    int e = pow(2,n)-1;
    for(int n=0; n<=e; n++){
        for(int i=log2(n); i>=0; i--){
            if(1 & (n >> i)){
                cout<<set[i]<<" ";
            }

        }
        cout<<endl;
    }
}
