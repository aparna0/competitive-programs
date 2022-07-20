#include<iostream>
#include<map>
#include<utility>
#include<regex>
//map is always in ascending by key
//functionality i same as set
//internally it implemented as BST ,therefore it is sorted
//and it take O(nlogn) time
using namespace std;
int main(){

    map<int,string> m,m2;                      //declaration

    m[1] = "aparna";                        //initialization
    m[1] = "ruchita";
    m[1] = "shreya";
                                                //accessing through key
    cout<<m[1]<<endl;                             //shreya


                                                    //insert({key,value})
    m.insert(pair<int,string>(2,"ruchita"));
    cout<<m[2]<<endl;

    m.insert({3,"aparna"});
    cout<<m[4]<<endl;                               //it return null

    int i;                                          //searching in 2 ways
    cout<<"enter key to search in m "<<endl;
    cin>>i  ;                                              //count(key)//occurrence of key
    if(m.count(i)){
        cout<<m[i]<<endl;
    }
    else{
       cout<<"key not found<<endl";
    }
    auto x = m.find(i);                                     //find()
    if(x != m.end()){
        cout<<m[i]<<endl;
    }
    else{
       cout<<"key not found<<endl";
    }

    cout<<"print value whose key is equal to or greater than 2\n";                    //print value whose key is equal to or greater than 2
    x = m.lower_bound(2);                                                            //lower bound
    cout<<(*x).second<<endl;

    m2 = m;                                                                 //copy by = operators

                                                                            //count number of characters in given string
    string input = "aparna chakrani mangalaram aparna";
    regex sep(" ");

    map<char,int> cnt;
    for(char i : input){
        cnt[i] += 1;
    }
    cout<<"char\tcount\n";
    for(auto i : cnt){
        if(i.first == ' ')
            cout<<"space"<<"\t"<<i.second<<endl;
        else
            cout<<i.first<<"\t"<<i.second<<endl;
    }

    return 0;
}
