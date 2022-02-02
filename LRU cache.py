class Node:
    def __init__(self,key,val):
        self.next=None
        self.prev=None
        self.key=key
        self.val=val
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail=None

class LRUCache:
    def __init__(self):
        self.cache={}
        self.current_size=0
        self.Max=3
        self.Recent_list=DoublyLinkedList()









    def get_hash(self,key):
        h=0
        for i in key:
            h+=ord(i)
        return h%100





