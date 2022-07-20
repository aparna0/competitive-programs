#include<bits/stdc++.h>
using namespace std;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin>>n;
    int a[n];
    for(int i=0; i<n; i++){
        cin>>a[i];
    }
    int fs = 0,res;
    for(int l=0; l<n; l++){
        for(int r=l; r<n; r++){
            int m = a[l];
            for(int j = l+1; j<=r; j++){
                if(m < a[j]){
                    m = a[j];
                }
            }
            res = m * (r-l+1);
            fs = (fs + res) % 1000000007;
        }
    }
    cout<<"\n"<<fs;
    return 0;
}
/*
for l in range(n):

    for r in range(l,n):
        #m = a[l]


        m = max(a[l:r+1])
        #print(m , (r - l + 1))
        res = m * (r - l + 1)
        finalr += res
        #finalr %= 1000000007

        #res %= 1000000007
#print(res)
print(finalr)
*/



