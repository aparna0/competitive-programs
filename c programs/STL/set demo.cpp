#include<iostream>
#include<set>
#include<algorithm>
using namespace std;
/*
Some basic functions associated with Set:
begin() – Returns an iterator to the first element in the set.
end() – Returns an iterator to the theoretical element that follows last element in the set.
rbegin()– Returns a reverse iterator pointing to the last element in the container.
rend()– Returns a reverse iterator pointing to the theoretical element right before the first element in the set container.
crbegin()– Returns a constant iterator pointing to the last element in the container.
crend() – Returns a constant iterator pointing to the position just before the first element in the container.
cbegin()– Returns a constant iterator pointing to the first element in the container.
cend() – Returns a constant iterator pointing to the position past the last element in the container.
size() – Returns the number of elements in the set.
max_size() – Returns the maximum number of elements that the set can hold.
empty() – Returns whether the set is empty.
insert(const g) – Adds a new element ‘g’ to the set.
iterator insert (iterator position, const g) – Adds a new element ‘g’ at the position pointed by iterator.
erase(iterator position) – Removes the element at the position pointed by the iterator.
erase(const g)– Removes the value ‘g’ from the set.
clear() – Removes all the elements from the set.
key_comp() / value_comp() – Returns the object that determines how the elements in the set are ordered (‘<‘ by default).
find(const g) – Returns an iterator to the element ‘g’ in the set if found, else returns the iterator to end.
count(const g) – Returns 1 or 0 based on the element ‘g’ is present in the set or not.
lower_bound(const g) – Returns an iterator to the first element that is equivalent to ‘g’ or definitely will not go before the element ‘g’ in the set.
upper_bound(const g) – Returns an iterator to the first element that will go after the element ‘g’ in the set.
equal_range()– The function returns an iterator of pairs. (key_comp). The pair refers to the range that includes all the elements in the container which have a key equivalent to k.
emplace()– This function is used to insert a new element into the set container, only if the element to be inserted is unique and does not already exists in the set.
emplace_hint()– Returns an iterator pointing to the position where the insertion is done. If the element passed in the parameter already exists, then it returns an iterator pointing to the position where the existing element is.
swap()– This function is used to exchange the contents of two sets but the sets must be of same type, although sizes may differ.
operator= – The ‘=’ is an operator in C++ STL which copies (or moves) a set to another set and set::operator= is the corresponding operator function.
get_allocator()– Returns the copy of the allocator object associated with the set.
*/
int main(){
    set<int> s;
    s = {1,5,2};
    s.insert(4);
    s.insert(5);
    s.insert(3);

    set<int> s2(s.begin(),s.end());             //coping set s to s2

    //cout<<s[0]<<endl;         not applicable

    for(auto i=s2.begin(); i!=s2.end(); i++){     //it automatically print in sorted manner
        cout<<*i<<' ';
    }
    cout<<endl;

    cout<<"size of set s is "<<s.size()<<endl;      //check size()

    cout<<"is set s is empty : "<<s.empty()<<endl;    //check is set empty or not

    s2.erase(s2.begin());                              //erase

    auto i =s.find(1);                                  //find()

    while(i!=s.end()){
        cout<<*i<<' ';
        ++i;
    }
    cout<<endl;

    s.erase(1);                                        //deleting element 1

    i =find(s.begin(),s.end(),5);                      //if element not found then it return last pointer of iterator
    while(i!=s.end()){
        cout<<*i<<' ';
        ++i;
    }
    cout<<endl;

    set<int> :: iterator it1 = s.lower_bound(2); //it will find element which is >= 2
    set<int> :: iterator it2 = s.upper_bound(10); //it will find element which is > 2
    cout<<"just greater or equal element to 2 is "<<*it1<<endl;     //if element is not present then it will 0
    cout<<"just greater element to 2 is "<<*it2<<endl;
    return 0;
}
