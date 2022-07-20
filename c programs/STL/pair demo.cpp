/*
declaring pair :
    pair<first_datatype, second_datatype> pair_name;

initializing pair :
    pair p1; //default
    pair p2(1,'a'); //create pair with different datatype
    pair p3(1,2); ////create pair with same datatype
    pair p4(p3);
*/

#include<iostream>
#include<utility>
using namespace std;
int main(){
                                                                //declaring and initializing pairs
    pair<int,float> p1;                                         //create pair with default value 0 and NUll
    pair<int,float> p2(1,'a');                                  //instead of a it takes ascii value of a
    pair<char,string> p3('a',"aparna");
    pair<int,float> p4(p2);

                                                                //accessing elements
    cout<<"1st element of p1 :"<<p1.first<<endl;
    cout<<"1st element of p1 :"<<p1.second<<endl;
    cout<<endl;
    cout<<"1st element of p2 :"<<p2.first<<endl;
    cout<<"1st element of p2 :"<<p2.second<<endl;
    cout<<endl;
    cout<<"1st element of p3 :"<<p3.first<<endl;
    cout<<"1st element of p3 :"<<p3.second<<endl;
    cout<<endl;
    cout<<"1st element of p4 :"<<p4.first<<endl;
    cout<<"1st element of p4 :"<<p4.second<<endl;
    cout<<endl;

    p1 = {1,1.5};                                               //initialization after declaration
    cout<<"After initialization of p1"<<endl;
    cout<<"1st element of p1 :"<<p1.first<<endl;
    cout<<"1st element of p1 :"<<p1.second<<endl;
    cout<<endl;

                                                                //updating values of pair
    p2.first = 0;
    p2.second = 5.5;
    cout<<"After updation of p2"<<endl;
    cout<<"1st element of p2 :"<<p2.first<<endl;
    cout<<"1st element of p2 :"<<p2.second<<endl;
    cout<<endl;

                                                                //comparison operators
    pair<int, float> p5;
    p5 = p1;
    cout<<"1st element of p5 :"<<p5.first<<endl;
    cout<<"1st element of p5 :"<<p5.second<<endl;
    cout<<endl;

    cout<<"is p1 and p5 same? :"<<(p1 == p5)<<endl;
    cout<<"is p1 and p2 same? :"<<(p1 == p2)<<endl;
    cout<<endl;

    cout<<"is p1 < p5 same? :"<<(p1 < p5)<<endl;                //it 1st check 1st element and if 1st element is same
    cout<<"is p1 < p2 same? :"<<(p1 < p2)<<endl;                //then only it will check 2nd element
    cout<<endl;

    cout<<"is p1 > p5 same? :"<<(p1 > p5)<<endl;                //it 1st check 1st element and if 1st element is same
    cout<<"is p1 > p2 same? :"<<(p1 > p2)<<endl;                //then only it will check 2nd element
    cout<<endl;

    cout<<"is p1 <= p5 same? :"<<(p1 <= p5)<<endl;                //it 1st check 1st element and if 1st element is same
    cout<<"is p1 <= p2 same? :"<<(p1 <= p2)<<endl;                //then only it will check 2nd element
    cout<<endl;

    cout<<"is p1 >= p5 same? :"<<(p1 >= p5)<<endl;                //it 1st check 1st element and if 1st element is same
    cout<<"is p1 >= p2 same? :"<<(p1 >= p2)<<endl;                //then only it will check 2nd element
    cout<<endl;

    return 0;
}
