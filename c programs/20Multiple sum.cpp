/*
for given positive x number, find sum of all multiples of 3 and 5 where multiple should be less than or equal to x.
for example, x = 12 then sum is 45{3+5+6+9+10+12}
*/
#include<iostream>
using namespace std;
int main(){
    int x;
    cout<<"enter value for x\t";
    cin>>x;
    int s3=0, s5=0, sum=0;
    for(int i=1; i<=x; i++){
        s3++;
        s5++;
        if(s3 == 3){
            sum += i;
            s3 = 0;
        }
        else if(s5 == 5){
            sum += i;
            s5 = 0;
        }
    }
    cout<<"sum is "<<sum;
    return 0;
}
