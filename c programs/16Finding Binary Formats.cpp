#include<iostream>
#include<math.h>
#include<stack>
using namespace std;

void printBinary(int);
void byDivisionOfTwo(int);

int main(){
    int n;
    cout<<"enter number";
    cin>>n;
    cout<<"binary format of "<<n<<" is ";
    for(int i=log2(n); i>=0; i--){
        if(1 & (n >> i)){
            cout<<1<<" ";
        }
        else{
            cout<<0<<" ";
        }
    }
    printBinary(n);
    byDivisionOfTwo(n);
    return 0;
}

void printBinary(int no){
    for(int n=0; n<=no; n++){
        cout<<"\n"<<n<<" -> ";
        for(int i=log2(n); i>=0; i--){
            if(1 & (n >> i)){
                cout<<1<<" ";
            }
            else{
                cout<<0<<" ";
            }
        }

    }
}

void byDivisionOfTwo(int no){
    int d = no;
    stack<int> s;
    while(d > 1){
        s.push(d%2);
        d /= 2;
    }
    s.push(1);
    cout<<"\n using division method "<<no<<" -> ";
    while(!s.empty()){
        cout<<s.top()<<" ";
        s.pop();
    }
}

