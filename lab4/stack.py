class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.head=None

    def push(self,node):
        if self.head==None:
            self.head=node
        else:
            node.next=self.head
            self.head=node

    def pop(self):
        if self.head==None:
            print("Stack is empty ")
        else:
            temp=self.head
            self.head=self.head.next
            temp=None
            
    def __str__(self):
        current=self.head
        nodes=[]
        while(current!=None):
            nodes.append(current.data)
            current=current.next
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
