class graph:
    def __init__(self,everypath):
        self.edges =everypath
        self.graph_dict={}
        for start, end in everypath:
            if start  in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
    def get_all_paths(self,start,end,path=[]):
        path = path +[start]
        if start==end:
            return [path]
        if start not in self.graph_dict:
            return []
        paths=[]
        for i in self.graph_dict[start]:
            if i not in path:
                d = self.get_all_paths(i, end, path)
                #print(d)
                for j in d:
                    paths.append(j)
        return paths
    def shortest_path(self,start,end,path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []
        shortest_path=None
        for i in self.graph_dict[start]:
            if i not in path:
                sp=self.shortest_path(i,end,path)
                if sp:
                    if shortest_path is None or len(sp)< len(shortest_path):
                        shortest_path=sp
        return sp


everypath=[('mumbai','paris'),('mumbai','dubai'),('paris','dubai'),('paris','NY'),('dubai','NY'),('NY','toronto')]
gr=graph(everypath)
print(gr.graph_dict)
print(gr.get_all_paths('mumbai','NY'))
print(gr.shortest_path('mumbai','NY'))