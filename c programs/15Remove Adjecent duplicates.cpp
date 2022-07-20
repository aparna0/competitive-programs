#include<iostream>
#include<string.h>
#include<algorithm>
using namespace std;

int main(){
    string str1, str2;
    cout<<"enter string \n";
    cin>>str1;

    do{
        str2 = str1;
        int i = 0;
        int n = str1.size();

        while(i < n){
            int j = i+1, f = 0 ;
            while(j < n && str1[i] == str1[j]){
                j++;
                f = 1;
            }
            if(f){
                auto e = find(str1.begin(),str1.end(),str1[i]);
                str1.erase(e, e+(j-i));
            }
            else{
                i++;
            }

        }

    }while(str1 != str2);

    cout<<"\n\n"<<str1;
    return 0;
}

/*
while(i < str1.size()){
               // cout<<"\nstr1[i]"<<str1[i]<<" "<<str1[i+1]<<"i "<<i;

            if(str1[i] == str1[i+1]){
                str1.erase(remove(str1.begin(),str1.end(),str1[i]),str1.end());
                cout<<"\n\t"<<str1;
            }
            else{
                i++;
            }
        cout<<"\n"<<str1;
        }

*/
