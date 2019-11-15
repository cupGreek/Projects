//Candy Shop With File Handling
#include<iostream>
#include<stdio.h>
#include<string.h>
#include<fstream>
using namespace std;

//Displenser Class
class dispenserType
{
 int numberOfItems, cost;
 char productName[20];

 public:
	dispenserType()
	{
	 numberOfItems = 0;
	 cost = 0;
	}

	/*dispenserType(int a, int b)
	{
	 numberOfItems = a;
	 cost = b;
	}*/

	void update(int a, int b, char* c)
	{
	 strcpy(productName,c);
	 numberOfItems = a;
	 cost = b;
	}

	char* getName()
	{
	 return productName;
	}

	int getCost()
	{
	 return cost;
	}

	int getNoOfItems()
	{
	 return numberOfItems;
	}

	void makeSale(int x)
	{
	 numberOfItems-=x;
        }
};

//Cash Register Class
class cashRegister
{
 int cashOnHand;

 public:
	cashRegister()
	{
	 cashOnHand = 500;
	}

	/*cashRegister(int a)
	{
	 cashOnHand = a;
	}*/

	void update(int a)
	{
	 cashOnHand = a;
	}

	int getCurrentBalance()
	{
	 return cashOnHand;
	}

	void acceptAmount(int a)
	{
	 cashOnHand+= a;
	}
};


//Show Selection Function
void showSelection(dispenserType dispenser[],int n)
{
 int i=0;
 for(;i<n;i++)
  cout<<endl<<i+1<<'.'<<dispenser[i].getName();
 cout<<"\n"<<i+1<<".End Shopping \nChoose your Product by entering the corresponding number: ";
}


//Sell Product Function
void sellProduct(dispenserType &dispenser, cashRegister &cashReg)
{

 int quantity, inStock, cash, cost;
 char confirm;
 cost = dispenser.getCost();
 inStock = dispenser.getNoOfItems();


 if(inStock == 0)
 {
  cout<<"\nThe Chosen Product is out of stock right now";
  return;
 }

 else
 {
  cout<<"\nEnter the quantity of "<<dispenser.getName();
  cin>>quantity;

  if(quantity>inStock)
  {
   cout<<"\nThe required quantity is not available right now, we can instead give you "<<inStock<<" units. Would you like to make the purchase?";
   cin>>confirm;
   if(confirm == 'y')
    quantity = inStock;
   else
    return;
  }
 }

  cout<<"\nThe total cost of your purchase is "<<cost*quantity;
  cout<<"\nInput your cash";
  cin>>cash;
  if(cash<cost*quantity)
  {
   cout<<"\nThe entered cash is not enough to make the purchase. Would you like to reduce the quantity to "<<int(cash/cost)<<" to best suite your budget? ";
   cin>>confirm;
   if(confirm == 'y')
   {
    quantity = int(cash/cost);
   }
   else
   {
    return;
   }
  }

  cost = quantity*cost;
  cout<<"\nThank you making the purchase. Here is your change: "<<cash-cost<<endl;
  cashReg.acceptAmount(cost);
  dispenser.makeSale(quantity);
}


//Main Function
int main()
{
 int y,n;
 cashRegister cash;
 dispenserType *dispenser;


//Reading from the file
 ifstream fin;
 fin.open("Candy.txt",ios::in);
 if(fin)
 {
  int temp1=0,temp2;
  char temp[25];
  fin>>temp1;
  cash.update(temp1);
  fin>>n;
  dispenser = new dispenserType[n];
  for(int i=0;i<n;i++)
  {
   fin>>temp;
   fin>>temp1>>temp2;
   dispenser[i].update(temp1,temp2,temp);
  }
 }

 else
 {
  dispenser = new dispenserType;
  n = 0;
 }
 showSelection(dispenser,n);
 cin>>y;

 while(y!=n+1)
 {
  if(y==0)
  {
   int temp1, temp2;
   char temp[25];
   cout<<"Current Balance is "<<cash.getCurrentBalance();
   cout<<"\nEnter the initial cash in Cash Register: ";
   cin>>temp1;
   cash.update(temp1);
   cout<<"\nNo.Of.Dispensers: ";
   cin>>n;
   dispenser = new dispenserType[n];
   for(int i=0;i<n;i++)
   {
    cout<<"\nEnter the product in the dispenser: ";
    cin>>temp;
    cout<<"\nEnter the Stock and Cost per unit of "<<temp<<"  :";
    cin>>temp1>>temp2; 
    dispenser[i].update(temp1,temp2,temp);
   }
  }
  else
  {
    if(y<=n)
     sellProduct(dispenser[y-1],cash);
    else
     cout<<"Invalid Input";
  }
  showSelection(dispenser,n);
  cin>>y;
 }
 //Writing onto the file
 ofstream fout;
 fout.open("Candy.txt",ios::out);
 fout<<cash.getCurrentBalance()<<endl;
 fout<<n<<endl;
 for(int i=0;i<n;i++)
 {
  fout<<dispenser[i].getName()<<endl<<dispenser[i].getNoOfItems()<<endl<<dispenser[i].getCost()<<endl;
 }
 fout.close();
 return 0;
}
