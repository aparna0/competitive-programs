#include<iostream>
#include<array>
#include<String>
#include<algorithm>
using namespace std;
/*
1. at() :- This function is used to access the elements of array.
2. get() :- This function is also used to access the elements of array. This function is not the member of array class but overloaded function from class tuple.
3. operator[] :- This is similar to C-style arrays. This method is also used to access array elements.
4. front() :- This returns the first element of array.
5. back() :- This returns the last element of array.
6. size() :- It returns the number of elements in array. This is a property that C-style arrays lack.
7. max_size() :- It returns the maximum number of elements array can hold i.e, the size with which array is declared. The size() and max_size() return the same value.
8.swap()
9. empty() :- This function returns true when the array size is zero else returns false.
10. fill() :- This function is used to fill the entire array with a particular value.
*/
int main(){
    //syntax : array<type,size> variableName
    array<string,5> a;
    string in;

    cout<<"enter 5 names "<<endl;
    for(int i=0;i<5;i++){
        cin>>in;
        a[i] = in;
    }
    cout<<"printing element using indexing"<<endl;
    for(int i=0;i<5;i++){
        cout<<a[i]<<endl;
    }
    cout<<endl;

    cout<<"printing element using at()"<<endl;
    for(int i=0;i<5;i++){
        cout<<a.at(i)<<endl;
    }
    cout<<endl;

    cout<<"printing element using get()"<<endl;
    cout << "The array elements are (using get()) : ";
    cout << get<0>(a) << " " << get<1>(a) << " ";
    cout << get<2>(a) << " " << get<3>(a) << " ";
    cout << get<4>(a);
    cout << endl;

    // Printing first element of array
    cout << "First element of array is : ";
    cout << a.front() << endl;

    // Printing last element of array
    cout << "Last element of array is : ";
    cout << a.back() << endl;

    // Printing number of array elements
    cout << "The number of array elements is : ";
    cout << a.size() << endl;

    // Printing maximum elements array can hold
    cout << "Maximum elements array can hold is : ";
    cout << a.max_size() << endl;

    sort(a.begin(),a.end());                        //sorting
    cout<<"after sorting"<<endl;
    for(int i=0;i<5;i++){
        cout<<a[i]<<endl;
    }
    cout<<endl;

    cout<<"max string"<<*(max_element(a.begin(),a.end()))<<endl;

    return 0;
}
