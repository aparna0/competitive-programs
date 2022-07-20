#include<iostream>
#include<deque>
#include<algorithm>                                       //functioning of deque is same as a vector
#include<vector>
using namespace std;
int main(){
    deque<int> dq;                                      //declaration of deque


    //dq.push(10);                                      //not applicable

                                                        //inserting elements in deque
    dq.push_back(3); //or dq.emplace_back(3)            //it insert at end
    dq.push_back(4);
    dq.push_front(2);//or dq.emplace_front(2)           //it insert at begin
    dq.push_front(1);

    dq.insert(dq.begin()+4,5);                          //it insert 5 at index 4

    vector<int> v(2,20);
    dq.insert(dq.end(),v.begin(),v.end());              //we can insert more than 1 elements(iteraor) in vector v
    cout<<"size of deque after update : "<<dq.size()<<endl;
    for(auto i : dq){
        cout<<i<<endl;
    }
    cout<<endl;


    cout<<"1st element in deque :"<<dq.front()<<endl;              //printing 1st element
    cout<<endl;

    cout<<"last element in deque :"<<dq.back()<<endl;              //printing last element
    cout<<endl;

    cout<<"size of deque before update : "<<dq.size()<<endl;

    dq[0] = 10;                                                     //update value at index 0
    dq[5] = 10;                                                     //it does not element or not through exception
    cout<<"size of deque after update : "<<dq.size()<<endl;

    sort(dq.begin(),dq.end());                                      //sorting elements in deque

                                                             //printing elements in queue
    cout<<dq[0]<<endl;                                       //we can access through index
    cout<<endl;
    cout<<dq.at(0)<<endl;                                       //we can access through at() function
    cout<<endl;
    for(auto i : dq){
        cout<<i<<endl;
    }
    cout<<endl;

    for(auto i=dq.rbegin(); i!=dq.rend(); ++i){              //printing in reverse
        cout<<*i<<endl;
    }
    cout<<endl;


                                                            //deleting elements in queue
    //dq.pop();                                             //not applicable
    dq.pop_front();                                         //delete 1st element
    dq.pop_back();                                          //delete last element


    cout<<"Element in deque after deletion "<<endl;
    for(auto i : dq){
        cout<<i<<endl;
    }
    cout<<endl;

    deque<int> dq2;

    dq2.assign(3,5);                                        //assign()

    dq.swap(dq2);                                           //swap()

    cout<<"Element in deque dq after swapping "<<endl;
    for(auto i : dq){
        cout<<i<<endl;
    }
    cout<<endl;

    dq.assign(dq2.begin(),dq2.end());                       //assign(iterator1, iterator2)

    cout<<"Element in deque dq after assignment dq2 to dq "<<endl;
    for(auto i : dq){
        cout<<i<<endl;
    }
    cout<<endl;

    cout<<"Size of dq : "<<dq.size()<<endl;

    dq.resize(10);                                          //resize(size)(resize and fill empty with 0)

    cout<<"Size of dq after resize : "<<dq.size()<<endl;
    cout<<"Element in deque dq after resize "<<endl;
    for(auto i : dq){
        cout<<i<<endl;
    }
    cout<<endl;

    cout<<"Element in deque dq after assignment dq2 to dq "<<endl;
    for(auto i : dq){
        cout<<i<<endl;
    }
    cout<<"element at index 1 is "<<dq.at(1)<<endl;

}
