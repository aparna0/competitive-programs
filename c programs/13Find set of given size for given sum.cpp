#include<iostream>
using namespace std;

long long N;
int maxKVal = 0;

void findMaxK(long long, int [], long long, int);

int main(){
    long long maxSum;
    int k;
    cout<<"enter size of resulting set, max sum and index\n";
    cin>>N>>maxSum>>k;

    int set[N];
    findMaxK(maxSum,set,N,k);
    cout<<"max Kth value is "<<maxKVal;
    return 0;
}
void findMaxK(long long cs, int set[], long long n, int k){
    if(cs == 0){
        for(int i=0 ;i<N; i++){
            cout<<set[i]<<" ";
        }
        if(set[k] > maxKVal ){
            maxKVal = set[k];
        }
        cout<<endl;
    }
    if(n == 0){
        return;
    }
    else{
        for(int i=1; i<= cs-(n-1); i++){
            if(N-n == 0){
                set[0] = i;
                findMaxK(cs-i,set,n-1,k);
            }
            else{
                if( abs(set[N-n-1] - i) <= 1 ){
                    set[N-n] = i;
                    findMaxK(cs-i,set,n-1,k);
                }
            }
        }
    }
}

