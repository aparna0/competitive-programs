
#include<iostream>
#include<vector>     //to create vector
#include<algorithm>

using namespace std;

int main(){
    cout<<"hello wold";

                                                        //declaring vector of type int
    vector<int> a;
    a = {2,1,3};

                                                        //accessing elements
    cout<<"\nfirst element : "<<a.front()<<endl;
    cout<<"\nlast element : "<<a.back()<<endl;
    cout<<"\n2nd element : "<<a[1]<<endl;
    cout<<"printing elements of a"<<endl;
    for(int j : a){                                     //we can also declare j as auto
            cout<<j<<' ';
    }
    cout<<endl;


                                                        //using data() pointer
    int* i = a.data();      //, returns the pointer of 1st element
    cout<<"\nfirst element : "<<*i<<endl;


    a.push_back(5);
    a.push_back(5);     //duplicates are allowed

    //begin()   returns iterator pointer to first
    //end()     returns iterator pointer to last
    //rbegin()
    //rend()
    //cbegin()
    //cend()
    //crbegin()
    //crend()
    //inserting element in vector
    for(auto i = a.rbegin(); i != a.rend(); ++i){
        cout<<*i<<' ';
    }
    cout<<'\n';
    for(auto i=a.cbegin(); i != a.cend(); ++i ){
        cout<<*i<<' ';
    }
    cout<<'\n';

    cout<<"size(length) of a is "<<a.size()<<endl;
    cout<<"current space allocated to a in the form of elements is "<<a.capacity()<<endl;
    cout<<"max elements that a can hold is "<<a.max_size()<<endl;
    a.resize(6);
    cout<<"size(length) of a is "<<a.size()<<endl;
    cout<<"is vector empty "<<a.empty()<<endl;

    vector<int> b(5,10);                        //it will create vector of 5 elements with  value 10

    b.assign(5,10);                           //it will create vector of 5 elements with  value 10

    for(int i=0;i<b.size();i++){
        cout<<b[i]<<' ';
    }
    cout<<endl;


    b[0] = 1;                                           //replace element at index 0

    b.insert(b.begin()+1,2);                            //insert 2 at index 1

    for(int i=0;i<b.size();i++){
        cout<<b[i]<<' ';
    }
    cout<<endl;
    cout<<"swapping"<<endl;
    a.swap(b);                                              //swap two vectors
    for(int i=0;i<b.size();i++){
        cout<<b[i]<<' ';
    }       //2 1 3 5 5 0
    cout<<endl;

    cout<<"\nis vector a and b equal?"<<(a == b)<<endl;

    //deleting elements in vector
    //pop_back()
    //erase()
    //clear()

    b.pop_back();
    b.erase(b.begin()+1);
    b.erase(b.begin()+1,b.begin()+2);
    for(int i=0;i<b.size();i++){
        cout<<b[i]<<' ';
    }
    cout<<endl;

    cout<<"occurance of 5in b :"<<count(b.begin(),b.end(),5);
    cout<<endl;

    bool x;
    x = binary_search(b.begin(),b.end(),5);    //binary search,return true or false
    cout<<"is 5 present in vector b ? "<<x<<endl;
    cout<<endl;

    sort(a.begin(),a.end());                        //sorting
    cout<<"after sorting vector a : ";
    for(int i=0;i<a.size();i++){
        cout<<a[i]<<' ';
    }
    cout<<endl;
    cout<<endl;

    auto y = find(a.begin(),a.end(),10);              //find
    cout<<"find f 10 in a : "<<*y<<endl;
    cout<<endl;

    vector<int> :: iterator it1 = lower_bound(a.begin(),a.end(),2); //it will find element which is >= 2
    auto it2 = upper_bound(a.begin(),a.end(),2);                   //it will find element which is > 2
    cout<<"just greater or equal element to 2 is "<<*it1<<endl;     //if element is not present then it will 0
    cout<<"just greater element to 2 is "<<*it2<<endl;
    cout<<"index difference between lower bound and upper bound "<<it2 - it1<<endl;
    cout<<"value difference between lower bound and upper bound "<<*it2 - *it1<<endl;
    cout<<endl;

    cout<<"After coping vector b to c : ";
    vector<int> c(b.begin(),b.end());                //coping vector b to c
    for(int i=0;i<c.size();i++){
        cout<<c[i]<<' ';
    }
    cout<<endl;





    b.clear();
    cout<<"size of b : "<<b.size()<<endl;

    vector<vector<int>> nestedVect;                                 //nested vector(vector inside vector)
    vector<int> v1 = {7,8,9,};
    nestedVect = {{1,2,3},{4,5,6,10}};

    //nestedVect.push_back(15);                                     //not applicable element must be vector
    nestedVect.push_back(v1);                                       //adding vector to nested vector
    nestedVect[0].push_back(15);

    nestedVect.erase(nestedVect.end());                             //erasing element in nested vector

    //cout<<nestedVect[0]<<endl;                                    //not applicable

    cout<<nestedVect[0][0]<<endl;                                   //accessing through indexing in nested vector

    cout<<"1st Element in nestedVect : ";                           //accessing elements in nestedVect
    for(auto i = nestedVect[0].begin(); i!=nestedVect[0].end(); ++i){
        cout<<*i<<' ';
    }
    cout<<endl;

    cout<<"last Element in nestedVect : ";
    int s = nestedVect.size()-1;                                    //to get index of last element <<nestedVect
     for(int i=0; i< nestedVect[s].size(); i++){
           cout<<nestedVect[s][i]<<' ';
     }
     cout<<endl;

     cout<<"printing all elements in nestedVector : "<<endl;
     for(auto i : nestedVect){
         for(int j : i){
            cout<<j<<' ';
         }
         cout<<endl;
     }
                                                                        //creating nested vector using different approaches

    //syntax : vector<type> variableName([[capacity], [initial value]]);   //[]indicates optional
    vector<vector<int>> vect2(3,vector<int>(5,0));                 //it creates vector with 3 vectors and each inner vector is with 5 zerozs
    cout<<"printing all elements in nested Vector vect2 : "<<endl;
    for(auto i : vect2){
         for(int j : i){
            cout<<j<<' ';
         }
         cout<<endl;
    }

    vector<vector<int>> vect3(3,vector<int>(5));
    for(int i=0; i<3; i++){
        for(int j=0; j<5; j++){
            vect3[i][j] = i*j;
        }
    }

    cout<<"printing elements of nested vector vect3 : "<<endl;
    for(int i=0; i<3; i++){
        for(int j=0; j<5; j++){
            cout<<vect3[i][j]<<' ';
        }
        cout<<endl;
    }

    return 0;
}
