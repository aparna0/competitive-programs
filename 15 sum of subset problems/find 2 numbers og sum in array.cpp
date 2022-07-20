#include<iostream>
using namespace std;
void findIndex(int, int [], int);
int main(){
    int n;
    cin>>n;
    int a[n];
    for(int i=0; i<n; i++){
        cin>>a[i];
    }
    int s;
    cin>>s;
    findIndex(n,a,s);
    return 0;
}
void findIndex(int n, int a[], int s){
    for(int i=0; i<n; i++){
        for(int j=i+1; j<n; i++){
            if(a[i] + a[j] == s){
                cout<<i<<" "<<j;
                return;
            }
        }
    }
}
