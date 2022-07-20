#include<iostream>
#include<vector>
using namespace std;
int getCatalon(int);

int main(){

    int no;
    cout<<"enter no to print Nth catalon number ";
    cin>>no;
    cout<<getCatalon(no);
    return 0;
}

int getCatalon(int no){
    vector<int> catalon(no+1,0);
    catalon[0] = catalon[1] = 1;
    for(int n=2; n<=no; n++){
        for(int i = 0; i<= n-1; i++){
            catalon[n] += catalon[i] * catalon[n-i-1];
        }
    }
    return catalon[no];
}
