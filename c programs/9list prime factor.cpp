#include<iostream>
#include<vector>
using namespace std;

int getListPrimeFactor(int);
vector<int> getListPrimeFactors(int); //using dynamic programming


int main(){
    int no;
    cout<<"enter no \t";
    cin>>no;
    cout<<"\nLeast prime factor of "<<no<<" is "<<getListPrimeFactor(no);

    cout<<"\nLeast prime factors up to "<<no<<" are \n";
    vector<int> factors;
    factors = getListPrimeFactors(no);
    cout<<"no\tleast prime factor\n";
    for(int i=0; i<=no; i++){
        cout<<i<<"\t"<<factors[i]<<endl;
    }

    return 0;
}

int getListPrimeFactor(int no){
    int res = no;

    if(no % 2 == 0){
         res = 2;
    }

    else{
        for(int i=3; (i*i)<=no; i=i+2){

            if(no%i == 0){
                res = i;
                break;
            }
        }
    }
    return res;
}

vector<int> getListPrimeFactors(int no){
    vector<int> res(no+1);
    for(int i=0; i<=no; i++){
        res[i] = i;
    }

    for(int i=2; (i*i)<=no; i++){
        if(res[i] == i){
            for(int j=i*i; j<=no; j=j+i){
                if(res[i] < res[j]){
                    res[j] = res[i];
                }
            }
        }
    }

    return res;
}
