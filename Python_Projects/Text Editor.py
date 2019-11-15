class node:
    def __init__(self,word):
        self.word=word
        self.next=None
        self.prev=None
        
class text:
    def __init__(self):
        self.head=None

    def addend(self,word):
        newnode=node(word)
        if self.head==None:
            self.head=newnode
            newnode.next=self.head
            self.head.prev=newnode
            
        else:
            posi=self.head
            while posi.next!=self.head:
                posi=posi.next
            if posi.prev.word==None:
                posi.prev=posi.prev.prev
                posi.prev.next=posi
            posi.next=newnode
            newnode.prev=posi
            self.head.prev=newnode
            newnode.next=self.head

    
    def add(self):
            text=input()
            text=text.split(" ")
            text.append(None)
            for i in text:
                self.addend(i)
        
    def traverse(self):
        posi=self.head
        while posi.word!=None:
            print(posi.word,end=' ')
            posi=posi.next
        print()
            
    def find(self,word,count):
        posi=self.head
        flag=0
        while posi.next!=self.head:
            if posi.word==word:
                flag=flag+1
                if count==flag:
                    return posi
                    break
                else:
                    pass
            posi=posi.next
        return posi

    def replace(self,word,replace,count):
        rep=self.find(word,count)
        if rep.word!=None:
            replace=node(replace)
            if rep==self.head:
                self.head=replace
            rep.prev.next=replace
            replace.next=rep.next
            rep.next.prev=replace
            replace.prev=rep.prev
        return rep
        


n=0
t=text()
while n!=5:
    n=int(input("1.Write 2.Find 3.Replace 4.Traverse 5.Exit: "))
    if n==1:
        t.add()
    
    elif n==2:
        word=input("Word to be searched: ")
        rep='\n'
        count=0
        while rep!=0:
            count=count+1
            rep=t.find(word,count)
            if rep.word==None:
                rep=0
            else:
                posi=rep
                for i in range(5,0,-1):
                    if posi.prev.word!=None:
                        posi=posi.prev
                while i<11 and posi.word!=None:
                    print(posi.word,end=' ')
                    posi=posi.next
                    i=i+1
                print()
                rep=input()
                
    elif n==3:
        rep='\n'
        word=input("To be replaced: ")
        replace=input("Replace with: ")
        while rep!=0:
            rep=t.replace(word,replace,1)
            if rep.word==None:
                rep=0
            else:
                rep=input()
                

    elif n==4:
        t.traverse()

    elif n==5:
        continue
    
    else:
        print("Invalid Input")
        
        
        
