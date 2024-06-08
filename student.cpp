#include<iostream>
#include<string>
using namespace std;
class student{
    public:
    int roll_no.=67675;
    int phone_no= 9680609735;
    string name= "HitikshaManoti"

    void getdata()
    {
        cout<<"Enter the roll_no."<<endl;
        cin>>roll_no.;
        cout<<"Enter the name"<<endl;
        cin>>name;
        cout<<"Enter the phone_no"<<endl;
        cin>>phone_no.;
        
    }
    void display()
    {
        cout<<"name is:"<<name<<endl;
        cout<<"roll_no. is:"<<roll_no<<endl;
        cout<<"phone_no is:"<<phone_no<<endl;

    }
};
int main(){
    student S;
    S.getdata();
    S.display();
    return 0;
}
