#include<bits/stdc++.h>
#include<map>
#include<vector>
#include<algorithm>
//#include<math.h>
using namespace std;
int getMinIndex(int [],int);
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n,k;
    cin>>n;
    cin>>k;

    string s;
    cin>>s;

    int c[n];
    for(int i=0; i<n; i++){
        cin>>c[i];
    }
    int op = 0;
    while(true){
        //cout<<"\n"<<s<<"\n";
        int f = 0;
        for(int i=0; i<(n-k); i++){

            int j = i+1;
            int cnt = 0;
            while(s[i] == s[j]){
                j++;
                cnt++;
            }
            //cout<<"cnt "<<cnt;
            if(cnt >= k){
                //cout<<"\nnot";
                f = 1;
                break;
            }
        }

        if(f){
            op++;
            int min_i = getMinIndex(c,n);
            c[min_i] = INT_MAX;
            s[min_i] = s[min_i]^1;
        }
        else{
            //cout<<"ok";
            break;
        }

    }
    cout<<"\nmin operations "<<op;
    return 0;
}

int getMinIndex(int c[],int n){
    int m = 0;
    for(int i=1; i<n; i++){
        if(c[i]<c[m]){
            m = i;
        }
    }
    return m;
}
/*
    map<int, vector<int>> m;
    int c;

    for(int i=0; i<n; i++){
        vector<int> v;
        cin>>c;

        auto x = m.find(c);
        if(x != m.end()){

            v = m[c];
            v.push_back(i);
            m[c] = v;
        }
        else{
            v.push_back(i);
            m[c] = v;
        }
    }

    for(int i=0;i<n;i++){
        //
        for(int i : m[i]){
            cout<<i<<" ";
        }
        cout<<"\n";


    }*/
