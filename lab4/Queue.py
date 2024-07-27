class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.head=None
        self.current=None

    def push(self,node):
        if self.head==None:
            self.head=node
            self.current=node
        else:
            self.current.next=node
            self.current=self.current.next

    def pop(self):
        if self.head==None:
            print("Queue is empty ")
        else:
            temp=self.head
            self.head=self.head.next
            temp=None
            
    def __str__(self):
        temp=self.head
        nodes=[]
        while(temp!=None):
            nodes.append(temp.data)
            temp=temp.next
        return "-> ".join(map(str,nodes))
    
s=Stack()
s.push(node(1))
s.push(node(2))
s.push(node(3))
s.push(node(4))
s.push(node(5))

print(s)

s.pop()

print(s)
