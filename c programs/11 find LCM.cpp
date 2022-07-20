#include<iostream>
#include<math.h>
using namespace std;

int findGCD(int, int);
int findLCM(int, int);

int main(){
    int a,b;
    cout<<"enter two numbers to find LCM\n";
    cin>>a>>b;
    cout<<"LCM is "<<(a*b)/findGCD(a,b)<<endl;                //method1


    cout<<"LCM is "<<findLCM(a,b)<<endl;                      //method2

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

int findLCM(int a, int b){
    int lcm;
    int s, l;
    if(a < b){
        s = a;
        l = b;
    }
    else if(b < a){
        s = b;
        l = a;
    }
    else{
        return a;
    }
    if(l % s == 0){
        lcm = l;
    }
    else{
        lcm = l + l;
        while(lcm % s != 0){
            lcm += l;
        }
    }
    return lcm;
}

