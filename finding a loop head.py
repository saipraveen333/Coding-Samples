class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
        def __init__(self):
            self.head = None

        def len(self):
            i = self.head
            count = 0
            while (i):
                count += 1
                i = i.next
            return count

        def print(self):
            i = self.head
            sum = ''
            count = 0
            while i:
                if count == self.len() - 1:
                    sum += str(i.data)
                    break
                sum += str(i.data) + '-->'
                i = i.next
                count += 1
            print(sum)
        def create_loop_at_element(self,k):
            i=self.head
            count=1
            while(count!=k):
                i=i.next
                count+=1
            temp=i
            while(i.next):
                i=i.next
            i.next=temp


        def insert_values(self, data_list):
            self.head = None
            for i in data_list:
                self.append(i)

        def append(self, data):
            if self.head is None:
                self.head = Node(data, None)
                return
            i = self.head
            while (i.next):
                i = i.next
            i.next = Node(data, None)
        def find_loop_node(self):
            i=self.head
            f=i.next
            s=i.next.next
            while(f!=s):
                f=f.next
                s=s.next.next

            temp=f
            i=self.head
            while(i!=temp):
                temp=temp.next
                i=i.next

            return i
        def len_of_loop(self):
            i=self.find_loop_node()
            temp=i
            count=1
            while(i.next!=temp):
                i=i.next
                count+=1
            return count


list = LinkedList()
list.insert_values([1,2,26,48,5,6])
list.print()
list.create_loop_at_element(4)
list.find_loop_node()
print(list.len_of_loop())
#list.print()







