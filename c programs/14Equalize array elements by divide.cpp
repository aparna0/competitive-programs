#include<iostream>
#include<vector>
#include<map>
using namespace std;

int main(){

    map<int, vector<int> > m;
    vector<int> v = {0};
    m[1] = v;

    return 0;
}
/*
int n,a[n],a2[n],r,d;
    cout<<"Enter size of array\t";
    cin>>n;
    cout<<"\n Enter "<<n<<" elements\n";
    for(int i=0; i<n; i++){
        cin>>a[i];
        a2[i] = a[i];
    }
    cout<<"\nEnter threshold value\t";
    cin>>r;
    cout<<"\nEnter divisor\t";
    cin>>d;

    for(int i=0; i<n; i++){
        cout<<a2[i]<<endl;
    }
    int f = 0;
    map<int,vector<int>> div;

    while(!f){
        for(int i=0; i<n; i++){
            if(div.count(a2[i])<0){
                vector<int> v;
                v.push_back(1);
                v.push_back(i);
                div[a2[i]] = v;
            }
            else{
                div[a2[i]][0] = div[a2[i]][0] + 1;
                (div[a2[i]]).push_back(i);
            }
            if(div[a2[i]][0] == r){
                f = a2[i];
                break;
            }
        }
        if(!f){
            for(int i=0; i<n; i++){
                a2[i] = a2[i] / d;
            }
        }
    }

    int cnt = 0;
    vector<int> v(div[f]);

    for(int i=1; i< v.size(); i++){
        while(v[i]!=f){
            cnt++;
            v[i]= v[i]/d;
        }
    }
*/
