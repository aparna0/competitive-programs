#include<iostream>
#include<stack>
using namespace std;
int main(){
    stack<int> st;                                      //declaring stack
    for(int i =1; i<=5; i++){
        st.push(i);                                     //push()
        cout<<"top : "<<st.top()<<endl;
    }
    st.emplace(10);                                     //emplace()

    cout<<"size of stack st : "<<st.size()<<endl;       //size()

    while(!st.empty()){                                 //empty()
        cout<<"top : "<<st.top()<<endl;
        st.pop();                                       //pop()
    }
    cout<<"is stack empty! "<<st.empty()<<endl;
    return 0;
}
