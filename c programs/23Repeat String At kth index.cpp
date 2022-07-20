#include<bits/stdc++.h>
#include<vector>
#include<algorithm>
using namespace std;
void printNicepermution(long long, long long [], int );

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    string is, cs;
    int k;
    //cout<<"enter string\t";

    cin>>is;
    cin>>k;
    int n = is.size();
    cout<<"n "<<n<<"\n";
    cs = is;
    //sort(cs.begin(),cs.end());
    //cout<<"\n"<<cs;
    do{
        cout<<"\ncs "<<cs;
        int f = 1;
        for(int i=0; i<n-k; i++){
            cout<<"\n"<<cs[i]<<" "<<cs[i+k];
            if(cs[i] != cs[i+k]){
                f = 0;
                break;
            }
        }
        cout<<" "<<f;
        if(f){
            cout<<cs;
            break;
        }
    }while(next_permutation(cs.begin(),cs.end()));


    return 0;
}
