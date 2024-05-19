class Node:
    id = -1
    def __init__(self, 
                 name: str, 
                 x: float, 
                 y:float
                ):
        self.name = name
        self.x = x
        self.y = y
        
    def print(self):
        print(f'id: {self.id} name: {self.name} x: {self.x} y: {self.y}')
        
class NodeList:
    # for문 사용 위해 추가 
    def __getitem__(self, index):
        return self.FnodeList[index]
    
    def __init__(self, FnodeList=[]):
        self.FnodeList = FnodeList 
    
    def get(self, id):
        return self.FnodeList[id] 
        
    def add(self, node: Node):
        self.FnodeList.append(node)
        self.FnodeList[-1].id = len(self.FnodeList) - 1
    
    def delete(self, id: int):
        self.FnodeList.pop(id)
        
    def update(self, id: int, node: Node):
        self.FnodeList[id] = node 
        
    def printAll(self):
        for node in self.FnodeList:
            node.print()