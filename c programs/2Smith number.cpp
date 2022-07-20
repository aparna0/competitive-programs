/*
number said to be smith number for given composite number
iff sum of digits of given number and sum of digit in all prime factors is eqaul

for example,

    no = 666
    sum of digits = (6+6+6) = 18
    prime factors = (2,3,3,37)
    sum of prime factors = (2+3+3+(3+7)) = 18
    sum of digits == sum of prime factors ,
        therefore given number is smith

steps ,
1)check given number is composite or not,
    if
        "No" then print("not smith no") and stop
    else
        proceed next step

2)find sum of digits of given number
3)find prime factor
4)find sum of digits prime factors
5)compare both sum
    if equal
        print(smith no)

    else
       print("not smith no")
*/
#include<iostream>
#include<vector>
using namespace std;

bool isCompositeNumber(int);
bool isSmithNumber(int);

int main(){
    int no;
    //take input number from user number
    cout<<"Enter number to check whether number is smith or not";
    cin>>no;

    if(isCompositeNumber(no)){

        if(isSmithNumber(no)){

            cout<<no<<" is smith number\n";
        }
        else{

        cout<<no<<" is not smith number\n";
    }
    }
    else{

        cout<<no<<" is not smith number\n";
    }
    return 0;
}

bool isCompositeNumber(int no){

    for(int i=2; (i*i)<=no; i++){
        if( no%i == 0){
            return true;
        }
    }
    return false;
}

bool isSmithNumber(int no){

    //find sum of digits of given number
    int sumOfDigits = 0;
    int nDash = no;
    while(nDash != 0){
        sumOfDigits += (nDash%10);
        nDash /= 10;
    }
    //cout<<"sum of digits of given number : "<<sumOfDigits<<endl;

    //finding factors for given number
    vector<int> factors;
    int i = 2;
    while(i <= no){
        if(no%i == 0){
            while(no%i == 0){
                factors.push_back(i);
                no /= i;
            }
        }
        i += 1;
    }
    /*cout<<"factors for given number\n";
    for(auto i : factors){
        cout<<i<<" ";
    }*/

    //finding sum of digits prime factors
    int sumOfFactor = 0;
    for(auto i : factors){
        nDash = i;
        while(nDash != 0){
            sumOfFactor += (nDash % 10);
            nDash /= 10;
        }
    }
    //cout<<" sum of digits prime factors "<<sumOfFactor<<endl;

    if(sumOfDigits == sumOfFactor)
        return true;

    return false;
}
