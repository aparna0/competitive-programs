#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
void printCombinations(vector<int>, int, int);
void getCombinations(vector<int>, int, int, int [], int , int );

int main(){
    int n, r;

    cout<<"Enter n\t";                                                  //take input for n
    cin>>n;

    vector<int> a(n);
    cout<<"Enter "<<n<<" elements \n";                                  //take input for n elements
    for(auto &i : a){
        cin>>i;
    }

    cout<<"Enter r\t";                                                  //take input for r
    cin>>r;

    //using recursion
    printCombinations(a,n,r);
    cout<<endl;

    return 0;
}

void printCombinations(vector<int> a, int n, int r){
    int com[r];
    getCombinations(a,n,r, com, 0, 0);
}

void getCombinations(vector<int> a, int n, int r, int com[], int currentR, int currentIndex){

    if(currentR == r) {
        for(int i=0; i<r; i++){
            cout<<com[i]<<' ';
        }
        cout<<endl;
        return;
    }

    if(currentIndex >= n){
        return;
    }

    else{
        com[currentR] = a[currentIndex];
        getCombinations(a, n, r, com, currentR+1, currentIndex+1);
        getCombinations(a, n, r, com, currentR, currentIndex+1);
    }
}
