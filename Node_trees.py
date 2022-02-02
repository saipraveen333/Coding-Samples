class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
    def add_child(self,data):
        data.parent=self
        self.children.append(data)
    def get_level(self,child):
        c=0
        p=child.parent
        while p:
            c+=1
            p=p.parent
        return c
    def print(self):
        if self.parent is None:
            spaces = ' ' * self.get_level(self)
        else:
            spaces='  '*self.get_level(self)+'|__'
        print(spaces+self.data)
        if self.children:
            for i in self.children:
                i.print()



def build_product_tree():
    root=TreeNode('Trees')

    branches = TreeNode('Branches')
    branches.add_child(TreeNode('stem'))
    branches.add_child(TreeNode('leaves'))

    trunk = TreeNode('Trunk')
    trunk.add_child(TreeNode('branches'))
    trunk.add_child(TreeNode('root'))

    root.add_child(trunk)
    root.add_child(branches)
    return root
roo=build_product_tree()
roo.print()






