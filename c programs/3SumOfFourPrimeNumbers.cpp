//by Goldbach's conjector in geeksforgeeks

#include<iostream>
using namespace std;
void findSet(int, int *);
bool isPrime(int);

int main(){

    //take input number from user
    int no;
    cout<<"Enter no ";
    cin>>no;

    if(no < 8){
        cout<<-1;
    }
    else{
        int a[4];

        if(no & 1){     //if no is odd
            a[0] = 2;
            a[1] = 3;
            findSet((no-5), a);
        }

        else{           //if no is even
            a[0] = 2;
            a[1] = 2;
            findSet((no-4), a);
        }

        for(int i=0; i<4; i++){
            cout<<a[i]<<" ";
        }
        cout<<endl;
    }
    return 0;
}

void findSet(int x, int *a){
    for(int i=2; i<=(x/2); i++){
        if(isPrime(i) && isPrime(x-i)){
            a[2] = i;
            a[3] = (x-i);
            return;
        }
    }
}

bool isPrime(int no){
    for(int i=2; (i*i)<=no; i++){
       if(no%i == 0)
            return true;
    }
    return true;
}
