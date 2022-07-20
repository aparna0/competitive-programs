

#include<iostream>
#include<math.h>
using namespace std;

int *createSTree(int [], int);
void constructSTree(int *, int [], int, int, int);
int getMid(int , int);
void getQuery(int *, int);
int getSum(int *, int , int, int, int, int);
void updateQuery(int *, int [], int);
void updateValue(int *, int , int , int , int, int);

int main(){

    int a[] = {3,4,6,8,2,3};
    int n = sizeof(a) / sizeof(int);
    //cout<<"size of array is "<<n<<endl;

    int *STree = createSTree(a, n);

    for(int i=0; i<13; i++){
        cout<<STree[i]<<"\t";
    }
    cout<<"segment tree created successfully...\n";

    getQuery(STree, n);
    updateQuery(STree, a, n);

    for(int i=0; i<13; i++){
        cout<<STree[i]<<"\t";
    }

    return 0;
}

int *createSTree(int a[], int n){
    int log = int(ceil(log2(n)));
    int sizeOfTree = 2 * (int)pow(2,log) - 1;
    int *STree = new int[sizeOfTree];
    constructSTree(STree, a, 0, n-1, 0);
    return STree;
}

void constructSTree(int *STree, int a[], int RS, int RE, int i){
    if(RS == RE){
        STree[i] = a[RS];
        return;
    }
    int mid = getMid(RS, RE);
    constructSTree(STree, a, RS, mid, 2*i+1);
    constructSTree(STree, a, mid+1, RE, 2*i+2);
    STree[i] = STree[2*i+1] + STree[2*i+2];
}

int getMid(int s, int e){
    return(s + (e - s) / 2);
}

void getQuery(int *STree, int n){
    int QS, QE;
    cout<<"Enter range in which you want to find minimum element\n";
    cin>>QS>>QE;
    if(QS < 0 || QE >= n || QS > QE){
        cout<<"wrong range!!!...";
        return;
    }
    cout<<"Minimum element is "<<getSum(STree, QS, QE, 0, n-1, 0)<<endl;
    int ch;
    cout<<"\nDo you want to continue?\t1.Yes\t2.No\n";
    cin>>ch;
    if(ch == 2)
        return;
    getQuery(STree, n);
}

int getSum(int *STree, int QS, int QE, int RS, int RE, int i){
    if( QS <= RS && QE >= RE){
        return STree[i];
    }
    if(QS > RE || QE < RS){
        return 0;
    }

    int mid = getMid(RS, RE);
    return ((getSum(STree, QS, QE, RS, mid, 2*i+1)) + (getSum(STree, QS, QE, mid+1, RE, 2*i+2)));
}

void updateQuery(int *STree, int a[], int n){

    int Ui, Uv;
    cout<<"enter index and value to update\n";
    cin>>Ui>>Uv;
    if(Ui < 0 || Ui > (n-1)){
        cout<<"invalid index";
        return;
    }

    int diff =  Uv - a[Ui];
    a[Ui] = Uv;

    cout<<diff;
    updateValue(STree, Ui, diff, 0, n-1, 0 );

    cout<<"\nupdate done"<<endl;

}

void updateValue(int *STree, int ui, int uv, int rs, int re, int i){
if(ui < rs || ui > re) return;
else{
cout<<STree[i]<<" "<<STree[i] + uv<<endl;
STree[i] += uv;
return;
}
int mid = getMid(rs, re);
updateValue(STree, ui, uv, rs, mid, 2*i+1 );
updateValue(STree, ui, uv, mid+1, re, 2*i+2 );
}
