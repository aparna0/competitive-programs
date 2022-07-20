#include<iostream>
#include<vector>
using namespace std;

vector<int> getFactors(int);

int main(){
    int no;
    cout<<"enter no to find prime factors of that no";
    cin>>no;
    vector<int> primeFactors = getFactors(no);
    for(int i : primeFactors){
        cout<<i<<endl;
    }
        return 0;
}

vector<int> getFactors(int no)
{
    vector<int> factors;
    while(no%2 == 0){
        factors.push_back(2);
        no /= 2;
    }
    for(int i=3; (i*i)<=no; i=i+2){
        while(no%i == 0){
        factors.push_back(i);
        no /= i;
        }
    }
    if(no > 2)  factors.push_back(no);
    return factors;
}
