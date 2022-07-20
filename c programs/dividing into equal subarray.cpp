#include<iostream>
#include<unordered_map>
using namespace std;
int main(){
    int n, i;
    //take inputs i.e N and array elements
    cout<<"Enter size of array\t";
    cin>>n;
    cout<<"\nenter "<<n<<" element\n";
    long long a[n],sum = 0;
    for(i=0; i<n; i++){
        cin>>a[i];
        sum += a[i];
    }
    cout<<endl;
    //cout<<sum<<endl;

    unordered_map<long long, int> m1,m2;
    m1[a[0]] = 1;

    for(i=1; i<n; i++)  m2[a[i]]++;
    /*
    cout<<m1[a[0]]<<endl;

    for(auto x : m2) cout<<x.first<<"\t"<<x.second<<endl;
    cout<<endl;*/

    //if sum is odd then we can divide it into 2 equal parts
    if(sum&1){
        cout<<"No";
        return 0;
    }
    else{
        sum /= 2;
        long long x;
        //cout<<sum<<endl;
        long long curSum = 0;

        for(i=0; i<(n-1); i++){
            curSum += a[i];
            if(curSum == sum){
                cout<<"Yes\n";
                return 0;
            }
            else if(curSum < sum){
                x = sum - curSum;
                if(m2[x]>0){
                    cout<<"Yes\n";
                    return 0;
                }
            }
            else{
                x = curSum - sum;
                if(m1[x]>0){
                    cout<<"Yes\n";
                    return 0;
                }
            }

            m1[a[i+1]]++;
            m2[a[i+1]]--;
        }
    }

    return 0;
}
