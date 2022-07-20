
#include<iostream>
#include<vector>
using namespace std;

bool isPrime(int);
void getPrimes(int);

int main(){
    vector<int> *primes;
    getPrimes(20);
    return 0;
}


//function to check where pass value is prime or not
bool isPrime(int no){
     if(no == 0 || no == 1)
        return false;
    for(int i=2; (i*i)<=no; i++){                       //using sieve
        if((no%i) == 0)
            return false;
    }
    return true;
}

//function to find prime numbers upto number no
void getPrimes(int no){             //sieve of eratothenes
     vector<int> tprimes(no, 1);
     tprimes[0] = tprimes[1] = 0;

     for(int i=2; (i*i)<=no; i++){
        if(tprimes[i]){
            for(int j=i*i; j<=no; j = j+i){
                tprimes[j] = 0;
            }
        }
     }

     for(int i=2; i<=no; i++){
        if(tprimes[i]){
            cout<<i<<" ";
        }
     }
}

