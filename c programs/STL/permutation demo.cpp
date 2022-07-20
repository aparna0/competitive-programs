#include<iostream>
#include<vector>
#include<algorithm>
//#include<stdio.h>
using namespace std;
void printPermutations(vector<int>, int n);
void getPermutations(vector<int>, int, int);
void usingInBuildFunction(vector<int>, int,vector<vector<int>> &);

int main(){
    int n;

    cout<<"Enter array size ";
    cin>>n;

    vector<int> a(n);
    cout<<"Enter "<<n<<" elements \n";
    for(auto &i : a){
        cin>>i;
    }

    //using recursion
    printPermutations(a,n);                                            //method1

    //using in build function
    vector<vector<int>> res;                                           //method2
    usingInBuildFunction(a,n,res);

    for(auto i : res){
        for(int j : i){
            cout<<j<<" ";
        }
        cout<<endl;
    }
    return 0;
}
void printPermutations(vector<int> a, int n){

    getPermutations(a,n,0);

}
void getPermutations(vector<int> a, int n, int i){
    //cout<<"ok";
    if(i == n){
        for(int i=0; i<n; i++){
            cout<<a[i]<<' ';
        }
        cout<<endl;
        return;
    }

    else{
        for(int j=i; j<n; j++){
            if(j!=i and a[j]==a[i])
                continue;
            swap(a[j],a[i]);
            getPermutations(a,n,i+1);

        }
    }
}

void usingInBuildFunction(vector<int> a,int n,vector<vector<int>> &res){
    sort(a.begin(),a.end());
    do{
        res.push_back(a);
    }while(next_permutation(a.begin(),a.end()));
}
