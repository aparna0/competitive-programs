#include<iostream>
#include<conio.h>
#include<string.h>
using namespace std;
struct Employee{
    int empNo;
    string ename;
    public:
        void setEmp(int no, string name){
            empNo = no;
            ename = name;
        }
        void displayEmp();
};
struct Manager:Employee{
    float salary;
    public :
        void computeSalary(float sal){
            salary = sal;
        }
        void display();
};

void Manager::display(){
    displayEmp();
    cout<<"\t"<<salary;
}

void Employee::displayEmp(){
    cout<<"\n"<<empNo<<"\t"<<ename;
}
int main(){
    Employee e1;
    e1.setEmp(1,"aparna");
    e1.displayEmp();
    Manager m1;
    m1.setEmp(2,"appi");
    m1.computeSalary(1000);
    m1.display();
    return 0;
}
