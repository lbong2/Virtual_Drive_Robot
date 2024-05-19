class Path:
    id = -1
    def __init__(self, fromNode, toNode, weight=1):
        self.fromNode = fromNode 
        self.toNode = toNode 
        self.weight = weight
        
    def print(self):
        print(f'id: {self.id} fromNode: {self.fromNode} toNode: {self.toNode}')
        
class PathList:
    # for문 사용 위해 추가 
    def __getitem__(self, index):
        return self.FpathList[index]
    
    def __init__(self, FpathList=[]):
        self.FpathList = FpathList 
    
    def get(self, id):
        return self.FpathList[id] 
        
    def add(self, path: Path):
        self.FpathList.append(path)
        self.FpathList[-1].id = len(self.FpathList)
    
    def delete(self, id: int):
        self.FpathList.pop(id)
        
    def update(self, id: int, path: Path):
        self.FpathList[id] = path 
        
    def printAll(self):
        for path in self.FpathList:
            path.print()