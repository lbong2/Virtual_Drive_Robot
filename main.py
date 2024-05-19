from base.base_node import * 
from base.base_path import * 
from base.base_graph import Graph 
from base.base_path_find import dijkstra
from base.base_db import MySQLDatabase

nList = NodeList()

tempN1 = Node('1001', 1.0, 2.0)
tempN2 = Node('1002', 2.0, 2.0)
tempN3 = Node('1003', 2.0, 1.0)
tempN4 = Node('1004', 1.0, 1.0)

nList.add(tempN1)
nList.add(tempN2)
nList.add(tempN3)
nList.add(tempN4)

nList.add(Node('1005', 3.0, 3.0))

nList.printAll()

pList = PathList()

tempN1 = Path('1001', '1002')
tempN2 = Path('1002', '1001')

pList.add(tempN1)
pList.add(tempN2)
pList.add(Path('1003', '1001'))

pList.printAll()

g = Graph(nodeList=nList, pathList=pList)

g.print()

d = dijkstra(g)

print(d.findPath('1001'))

mysql = MySQLDatabase('localhost', 'robot_db', 'root', 'dlrudqhd00@')

print(mysql.select('select * from main_node_tb;'))