#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include<stack>
using namespace std;
/*
1)sort(first_iterator, last_iterator)
2)reverse(first_iterator, last_iterator)
3)min_element(first_iterator, last_iterator)
4)max_element(first_iterator, last_iterator)
5)count(first_iterator, last_iterator, value)
6)accumulate(first_iterator, last_iterator, initial sum value)
7)find(first_iterator, last_iterator, value)
8)binary_search(first_iterator, last_iterator, value)
9)lower_bound(first_iterator, last_iterator, value)
10)upper_bound(first_iterator, last_iterator, value)
11)next_permutation(first_iterator, last_iterator)
12)prev_permutation(first_iterator, last_iterator)
13)distance()
*/

int main(){

    vector<int> vect = {1,7,5,3,2};
    set<int> s = {1,7,5,3,2};
    stack<int> st ;//= {1,7,5,3,2}

    for(auto a : s){
        st.push(a);
    }


    return 0;
}
