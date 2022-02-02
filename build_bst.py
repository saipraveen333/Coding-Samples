class BSTNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def add_child(self,data):
        if self.data==data:
            return 'the number is already present'
        if data<self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=BSTNode(data)
        if data>self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=BSTNode(data)
    def in_order_traverse(self):
        a=[]
        if self.left:
            a+=self.left.in_order_traverse()
        a=a+[self.data]
        if self.right:
            a+=self.right.in_order_traverse()
        return a
    def pre_order_traverse(self):
        a = [self.data]

        if self.left:
            a += self.left.pre_order_traverse()
        if self.right:
            a += self.right.pre_order_traverse()
        return a
    def post_order_traverse(self):
        a=[]
        if self.left:
            a += self.left.post_order_traverse()
        if self.right:
            a += self.right.post_order_traverse()
        a=a+[self.data]
        return a

    def build_tree(self,z):
        root = b

        for i in z[1:]:
            root.add_child(i)
        return root
    def min(self):
        if  self.left is None:
            return self.data
        else:
            return self.left.min()
    def max(self):
        if not self.right:
            return self.data
        else:
            return self.right.max()
    def remove(self,val):
        if val<self.data:
            if self.left:
                print(self.left.data)
                self.left=self.left.remove(val)
        elif val>self.data:
            if self.right:
                print(self.right.data)
                self.right=self.right.remove(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            minval=self.right.min()
            self.data=minval
            self.right=self.right.remove(minval)
        return self




z=[15,12,7,14,27,20,23,88]
b=BSTNode(z[0])
print(b.build_tree(z).remove(12).in_order_traverse())





