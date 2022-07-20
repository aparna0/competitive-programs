#include<iostream>
#include<math.h>
using namespace std;

int findGCD(int, int);

int main(){
    int a,b;
    cout<<"enter two numbers to find GCD\n";
    cin>>a>>b;
    cout<<"GCD is "<<findGCD(a,b);

    return 0;
}

int findGCD(int a, int b){              //using Euclidean algorithm for GCD
    if(b == 0){
        return a;
    }
    else{
        return findGCD(b, a%b);
    }
}
