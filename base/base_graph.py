from base.base_node import *
from base.base_path import * 


class Graph:
    FGraph = {}
    
    def __init__(self, nodeList: NodeList, pathList: PathList):
        
        for node in nodeList:
            self.FGraph[node.name] = {}
             
        for path in pathList:
            self.FGraph[path.fromNode][path.toNode] = path.weight
            
    def print(self):
        print(self.FGraph)    