from base import * 
import json 

def init_sql() -> MySQLDatabase:
    
    with open('auth.json') as f:
        data = json.load(f)
    sql = MySQLDatabase(**data)
    return sql
    
def init_node(sql: MySQLDatabase) -> NodeList:
    datas = sql.select('select * from main_node_tb;')
    nodes = NodeList()
    
    for data in datas:
        nodes.add(Node(data[1], data[2], data[3]))
    return nodes

def init_path(sql: MySQLDatabase) -> PathList:
    datas = sql.select('select * from main_path_tb;')
    
    paths = PathList()
    
    for data in datas:
        paths.add(Path(data[1], data[2], data[3]))
    return paths