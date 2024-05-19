from base import * 
from utills.utill_initial import *

sql = init_sql()
nodes = init_node(sql)
paths = init_path(sql)

nodes.printAll()
paths.printAll()