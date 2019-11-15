class cqueue:
    def __init__(self):
        self.limit=int(input("Enter the limit of the list"))
        self.list=[]
        self.front=None
        self.rear=None

    def isempty(self):
        if len(self.list)==0:
            return 1
        else:
            return 0
        
    def isfull(self):
        if len(self.list)==self.limit:
            return 1
        else:
            return 0
        
    def enqueue(self,element):
        if self.isfull():
            print("Overflow")
        else:
            if self.front==None and self.rear==None:
                self.front=self.rear=0
            elif self.rear==self.limit and len(self.list)!=self.limit:
                self.rear=0
            else:
                self.rear=self.rear+1
            self.list.append(element)

    def dequeue(self):
        if self.isempty():
            print("Underflow")
        else:
            if self.front==self.rear:
                self.front=self.rear=None
            elif self.front==self.limit and len(self.list)!=self.limit:
                self.front=0
            else:
                self.front=self.front+1
            return self.list.pop(0)
            

queue=cqueue()
while not(queue.isfull()):
    queue.enqueue(input("Name: "))
print(queue.list)
    
while not(queue.isempty()):
    j=int(input("Enter the number of times the ball is to passed"))
    while j!=0:
        queue.enqueue(queue.dequeue())
        j=j-1
    print(queue.dequeue())
    print(queue.list)
            
                

    
