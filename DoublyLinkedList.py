class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_forward(self):
        l=''
        i=self.head
        if i is None:
            return
        count=0
        while i:
            if count==self.len()-1:
                l+=str(i.data)
                break
            l+=str(i.data)+'<-->'
            i=i.next
            count+=1
        print(l)
    def print_backward(self):
        l=''
        i=self.head
        if i==None:
            return 'it\'s an empty list'
        while i.next:
            i = i.next
        while(i):
            l+=str(i.data)+'<-->'
            i=i.prev
        print(l)
    def len(self):
        i=self.head
        count=0
        while(i):
            count+=1
            i=i.next
        return count
    def append(self, data):
        if self.head is None:
            self.head=Node(data,None,None)
            return
        i = self.head
        while (i.next):
            i = i.next
        i.next = Node(data, None,i)

    def insert_values(self,data_list):
        self.head=None
        for i in data_list:
            self.append(i)
    def remove_value(self,data):
        i = self.head
        if i == Node(data, i.next):
            self.head=i.next
            return
        while (i):
            if i.next.data == data:
                i.next = i.next.next
                break
            i = i.next
    def insert_before_value(self,data_after_value,data_to_insert):
        i=self.head
        while(i.next):
            if i.next.data==data_after_value:
                i.next=Node(data_to_insert,i.next)
                break
            i=i.next

    def insert_after_value(self, data_before_value, data_to_insert):
        i = self.head
        while (i):
            if i.data == data_before_value:
               i.next = Node(data_to_insert, i.next)
            i = i.next

    def remove_and_insert(self,data_after_value,data_to_insert):
        self.remove_value(data_to_insert)
        self.insert_before_value(6,3)

    def set_as_head(self, data):
        self.head = Node(data, self.head)

    def set_to_head(self,data):
        self.remove_value(data)
        self.head = Node(data, self.head)

    def remove_values(self,data):
        i = self.head
        if i.data ==data:
            self.head = i.next
        while (i):
            if i.next.data == data:
                i.next = i.next.next
            i = i.next
    def search(self,data):
        i=self.head
        while(i):
            if i.data==data:
                return True

            i=i.next
        return False
l=DoublyLinkedList()
l.insert_values([1,2,3,4,5])
#l.print_backward()
l.print_forward()
l.set_to_head(4)
l.append(6)
l.remove_and_insert(6,3)
l.insert_after_value(6,3)
l.set_as_head(3)
l.remove_values(3)
l.remove_value(2)
l.print_forward()
print(l.search(8))


