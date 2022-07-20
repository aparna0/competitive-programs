#include<iostream>
#include<queue>
using namespace std;
int main(){
    queue<int> q;                                          //declaring queue

    for(int i=0;i<3;i++){
        q.push(i);                                          //adding elements in queue
    }

    q.emplace(4);                                           //emplace()

    cout<<"1st element in queue :"<<q.front();              //printing 1st element
    cout<<endl;

    cout<<"last element in queue :"<<q.back();              //printing last element
    cout<<endl;

    q.pop();                                                //delete 1st element in queue

    //q[5]= 5;  or cout<<q[0]                               //not applicable

                                                            //printing elements in queue
    cout<<"Elements in queue : "<<endl;
    queue<int> tempq = q;
    while(!tempq.empty()){                                  //empty()
        cout<<tempq.front()<<' ';                           //front()
        tempq.pop();                                        //pop()
    }
    cout<<endl;

    /*                                                      //begin() and end() are not member functions of queue
    for(auto i=q.begin(); i!=q.end(); ++i){
        cout<<*i<<endl;
    }
    for(auto i : dq){
        cout<<i<<endl;
    }*/


    cout<<"size of queue q : "<<q.size();                   //size()
    cout<<endl;

    q.swap(tempq);                                          //swap()
    cout<<"After wapping ...";
    cout<<endl;

    if(q.empty()){
        cout<<"q is empty !!!"<<endl;
    }
    return 0;
}
