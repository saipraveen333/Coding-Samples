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
    def print(self,r):
        i=self.data.find('(')
        j=self.data.find(')')
        if r=='name':
            self.data=self.data[:i]
        if r=="designation":
            self.data=self.data[i+1:j]

        if self.parent is None:
            spaces = ' ' * self.get_level(self)
        else:
            spaces='  '*self.get_level(self)+'|__'
        print(spaces+self.data)
        if self.children:
            for i in self.children:
                i.print(r)



def build_product_tree():
    root=TreeNode('Nilupul(CEO)')

    branches = TreeNode('chinmay(CTO)')
    stems = TreeNode('Vishwa(INF head)')
    branches.add_child(stems)
    branches.add_child(TreeNode('Aamir(A Head)'))

    stems.add_child(TreeNode('Dhawal(CM)'))
    stems.add_child(TreeNode('Abhi(App Manager)'))

    trunk = TreeNode('Gels(HR Head)')
    trunk.add_child(TreeNode('Peter(Recruit Manager)'))
    trunk.add_child(TreeNode('Waqas(Policy manager)'))

    root.add_child(trunk)
    root.add_child(branches)
    return root
build_product_tree().print('designation')




