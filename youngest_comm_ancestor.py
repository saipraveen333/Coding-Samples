class graph:
    def __init__(self,data):
        self.data=data
        self.dict={}
        for start, end in tup:
            if start in self.dict:
                self.dict[start].append(end)
            else:
                self.dict[start] = [end]
    def get_all_paths(self,start,end,path=[]):
        path = path +[start]
        if start==end:
            return [path]
        if start not in self.dict:
            return []
        paths=[]
        for i in self.dict[start]:
            if i not in path:
                d = self.get_all_paths(i, end, path)
                #print(d)
                for j in d:
                    paths.append(j)
        return paths
def youngest_common_ancestor(top_anc,first_des,second_des):
    path1=gr.get_all_paths(first_des,top_anc)
    path2=gr.get_all_paths(second_des,top_anc)
    for i in path2[0]:
        if i in path1[0]:
            if i is not first_des:
                return i



tup=[('B','A'),('C','A'),('D','B'),('E','B'),('F','C'),('G','C'),('H','E'),('I','E')]

gr=graph(tup)
print(gr.dict)
print(youngest_common_ancestor('A','I','H'))
