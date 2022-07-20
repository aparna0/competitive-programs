#include<iostream>
#include<math.h>
using namespace std;

int *createSTree(int [], int);
void constructTree(int *, int [], int, int, int);
int getMid(int, int);
void getQuery(int *, int);
int getMin(int *, int, int, int, int, int);
void updateQuery(int *, int [], int);
//void updateValue(int *, int [], int ,int,int );
void updateValue(int *, int , int, int, int, int);

int main(){
    int a[] = {1,3,2,-2,4,5};
    int n = sizeof(a)/sizeof(int);
    //cout<<"size of array is "<<n<<endl;

    int *STree = createSTree(a, n);
    /*
    for(int i=0; i<13; i++){
        cout<<STree[i]<<"\t";
    }*/
    cout<<"segment tree constructed successfully\n";

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
    //cout<<"size of segment tree is "<<sizeOfTree<<endl;

    int *STree = new int[sizeOfTree];
    constructTree(STree, a, 0, n-1, 0);
    return STree;
}

void constructTree(int *STree, int a[], int RS, int RE, int i){
    //cout<<"ok";
    if(RS == RE){
        STree[i] = a[RS];
        return;
    }

    int mid = getMid(RS, RE);
    constructTree(STree, a, RS, mid, 2*i+1);
    constructTree(STree, a, mid+1, RE, 2*i+2);
    STree[i] = min(STree[2*i+1], STree[2*i+2]);
    return ;
}

int getMid(int s, int e){
    return (s + (e - s) / 2);
}

void getQuery(int *STree, int n){
    int QS, QE;
    cout<<"Enter range in which you want to find minimum element\n";
    cin>>QS>>QE;
    if(QS < 0 || QE >= n || QS > QE){
        cout<<"wrong range!!!...";
        return;
    }
    cout<<"Minimum element is "<<getMin(STree, QS, QE, 0, n-1, 0)<<endl;
    int ch;
    cout<<"Do you want to continue?\t1.Yes\t2.No\n";
    cin>>ch;
    if(ch == 2)
        return;
    getQuery(STree, n);
}

int getMin(int *STree, int QS, int QE, int RS, int RE, int i){
    //cout<<"ok\n";
    if(QS <= RS && QE >= RE){
        return STree[i];
    }

    if(QS > RE || QE < RS){
        return INT_MAX;
    }

    int mid = getMid(RS,RE);
    return (min( getMin(STree, QS, QE, RS, mid, 2*i+1), getMin(STree, QS, QE, mid+1, RE, 2*i+2)));
}

void updateQuery(int *STree, int a[], int n){

    int Ui, Uv;
    cout<<"enter index and value to update\n";
    cin>>Ui>>Uv;
    if(Ui < 0 || Ui > (n-1)){
        cout<<"invalid index";
        return;
    }
    a[Ui] = Uv;
    updateValue(STree, Ui, Uv, 0, n-1, 0 );

    cout<<"\nupdate done"<<endl;
}

void updateValue(int *STree, int ui, int uv, int RS, int RE, int i){
    if(ui < RS || ui > RE) return;
    if(RS == ui && RE == ui){
        STree[i] = uv;
        return;
    }
    int mid = getMid(RS, RE);
    updateValue(STree, ui, uv, RS, mid, 2*i+1);
    updateValue(STree, ui, uv, mid+1, RE, 2*i+2);
    STree[i] = min(STree[2*i+1], STree[2*i+2]);
}

/*
void updateValue(int *STree, int a[], int RS,int RE,int i){
   if(RS == RE){
        STree[i] = a[RS];
        return;
    }

    int mid = getMid(RS, RE);
    updateValue(STree, a, RS, mid, 2*i+1);
    updateValue(STree, a, mid+1, RE, 2*i+2);
    STree[i] = min(STree[2*i+1], STree[2*i+2]);
}*/
