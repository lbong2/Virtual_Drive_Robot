from base.base_db import MySQLDatabase
import json


with open('map.json') as f:
    data = json.load(f)
print(type(data))

nodelist = data['nodeList']
pathlist = data['linkList']

q = MySQLDatabase('localhost', 'robot_db', 'root', 'dlrudqhd00@')

q.delete('delete from robot_db.main_node_tb where NODE_ID >= 1', '')
q.delete('delete from robot_db.main_path_tb where PATH_ID >= 1', '')
for i, v in enumerate(nodelist):
    q.insert('insert into robot_db.main_node_tb values(%d, %s, %f, %f, \'\')' % (i+1, v['name'], float(v['position']['x']), float(v['position']['y'])))
    
for i, v in enumerate(pathlist):
    from_node = v['name'].split('_')[1]
    to_node = v['name'].split('_')[2]
    q.insert('insert into robot_db.main_path_tb values(%d, %s, %s, 1, \'\')' % (i+1, from_node, to_node))