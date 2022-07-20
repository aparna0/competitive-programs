#include<iostream>
using namespace std;
int main(){
    int n;
    cout<<"enter number of cities\t";
    cin>>n;
    int tickets[n];
    cout<<"enter ticket costs\n";
    for(int i=0; i<n; i++){
        cin>>tickets[i];
    }
    int current_ticket = INT_MAX;
    int total_cost = 0;
    for(int i=0; i<n; i++){
        if(tickets[i] < current_ticket){
            current_ticket = tickets[i];
        }
        total_cost += current_ticket;
    }
    cout<<"\ntotal traveling cost is "<<total_cost;
    return 0;
}
