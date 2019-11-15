#include<fstream>
#include<iostream>
using namespace std;

class student
{
 char name[25];
 static long unsigned int temp;
 long unsigned int roll;
 int marks[6];
 float total, avg;

 void calc()
 {
  total = 0;
  for(int i = 0;i<6;i++)
	total+=marks[i];
  avg = total/6;
 }

 public:
	student()
	{
	 roll = ++temp;
	  for(int i = 0;i<6;i++)
		marks[i] = 0;
	  total = 0;
	  avg = 0;
	}

	student(ifstream &fin)
	{
	 if(fin)
	 {
	  fin>>name;
	  fin>>roll;
	  for(int i = 0;i<6;i++)
	     fin>>marks[i];
	  fin>>total>>avg;
	 }
	 else
	 {
	  roll = ++temp;
	  for(int i = 0;i<6;i++)
		marks[i] = 0;
	  total = 0;
	  avg = 0;
	 }
	}

	void getdata()
	{
	 cout<<"\nEnter the name of the Student ";
	 cin>>name;
	 cout<<"\nEnter the marks of the student ";
	 for(int i = 0; i<6;i++)
		cin>>marks[i];
	 calc();
	 cout<<roll;
	}

	void writedata(ofstream &fout)
	{
	 if(fout)
	 {
	  fout<<name<<endl;
	  fout<<roll<<endl;
	  for(int i = 0;i<6;i++)
		fout<<marks[i]<<endl;
	  fout<<total<<endl<<avg<<endl;
	 }
	 else
		cout<<"File doesn't exist";
	}

	int compare(int a)
	{
	 if(roll==a)
	   return 1;
	 else
	   return 0;
	}

	void showdata()
	{
	 cout<<"\nName: "<<name<<"\nRoll.No: "<<roll<<"\nTotal: "<<total<<"\nAverage: "<<avg;
	}
};

long unsigned int student::temp;

int main()
{
 student *stud;
 int choice=0;
 cout<<"\n1.Add new Student \n2.Show details of student \n3.Exit";
 cin>>choice;
 while(choice!=3)
 {
  switch(choice)
  {
   case 1:
	{
	 ofstream fout;
	 fout.open("Student.txt",ios::app);
	 student stu;
	 stu.getdata();
	 stu.writedata(fout);
	 break;
	}

   case 2:
	{
	 ifstream fin;
	 int i;
	 stud = new student[100];
	 fin.open("Student.txt",ios::in);
	 for(i = 0;!(fin.eof()); i++)
	 {
		stud[i]=student(fin);
		if(fin.eof())
		    break;
	 }
	 long unsigned int roll;
	 cout<<"\nEnter the roll number of the student";
	 cin>>roll;
	 for(int j = 0;j<i;j++)
	 {
	  if(stud[j].compare(roll))
	  {
	   stud[j].showdata();
	   break;
	  }
	 }
	 break;
	}
   default:
	 cout<<"\n Invalid Input";
  }
 cout<<"\n1.Add new Student \n2.Show details of student \n3.Exit";
 cin>>choice;
 }
 return 0;
}
