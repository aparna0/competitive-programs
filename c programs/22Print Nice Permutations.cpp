//#include<iostream>
#include<algorithm>
#include<vector>
#include<bits/stdc++.h>
using namespace std;
void printNicepermution(long long, long long [], int );

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    long long no;
    cin>>no;

    long long set[4];
    //printNicepermution(no, set, 0);

    vector<long long> a;
    for(long long i=1; i<=no; i++){
        a.push_back(i);
        set[i] = i;
    }

    long long cnt = 0;
    sort(a.begin(), a.end());
    do{
        int f = 1;
        for(int i=0; i<no; i++){
            if(i == 0){
                if(a[i]%2 != a[i+1]%2){
                    f = 0;
                    break;
                }
            }
            else if(i == no-1){
                if(a[i]%2 != a[i-1]%2){
                    f = 0;
                    break;
                }
            }
            else{
                if( a[i]%2 != a[i-1]%2 and a[i]%2 != a[i+1]%2){
                    f = 0;
                    break;
                }
            }
        }
        if(f){
            cnt++;
        }
    }while(next_permutation(a.begin(),a.end()));
    cout<<cnt;
    return 0;
}

void printNicepermution(long long n, long long set[], int ci ){
    cout<<"ci "<<ci;
    if(ci == n){
        for(int i=0; i<n; i++){
            cout<<set[i]<<" ";
        }
        cout<<"\n";
        return ;
    }
    else{
        for(int i=ci; i<n; i++){
            int f = 1;
            if(ci == 0){
                if(set[i]%2 != set[ci+1]%2){
                    f = 0;
                    break;
                }
            }
            else if(ci == n-1){
                if(set[i]%2 != set[ci-1]){
                     f = 0;
                    break;
                }
            }
            else{
                if(set[i]%2 != set[ci-1] && set[i] != set[ci+1]){
                     f = 0;
                    break;
                }
            }
            if(f){
                swap(set[i],set[ci]);
                cout<<"\nok";
                printNicepermution(n, set, ci+1);
            }
        }
    }
}
