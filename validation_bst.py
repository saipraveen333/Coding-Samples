
class BSTNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def add_child(self,data):
        if data==self.data:
            return
        if data>self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=BSTNode(data)
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BSTNode(data)
    def in_order_traverse(self):
        a=[]
        if self.left:
            a+=self.left.in_order_traverse()
        a=a+[self.data]
        if self.right:
            a+=self.right.in_order_traverse()
        return a

    def build_tree(self,l):
        root = BSTNode(l[0])
        for i in l[1:]:
            root.add_child(i)

        return root
    def is_valid(self):
        m=bn.build_tree(l).in_order_traverse()
        m[5] = 4

        for i in range(len(m)-1):
            if m[i]<m[i+1]:
                continue
            else:
                return False
        return True


l=[5,2,7,3,1,6,8]
bn=BSTNode(l[0])
bn.build_tree(l)
print(bn.build_tree(l).in_order_traverse())
print(bn.is_valid())






