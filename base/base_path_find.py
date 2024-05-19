from abc import abstractmethod
import heapq
from base.base_graph import Graph
from queue import PriorityQueue


class BasePathFind:
    
    @abstractmethod
    def findPath():
        pass
    
    @abstractmethod
    def findPathAvoidBlock():
        pass
    

class dijkstra(BasePathFind):
    pq = PriorityQueue()
    def __init__(self, graph: Graph):
        self.graph = graph.FGraph
        
    def findPath(self, start):
        distances = {node: float('inf') for node in self.graph}  # start로 부터의 거리 값을 저장하기 위함
        distances[start] = 0  # 시작 값은 0이어야 함
        prev = {node: None for node in self.graph}
        
        self.pq.put((distances[start], start))
        # heapq.heappush(queue, [distances[start], start])  # 시작 노드부터 탐색 시작 하기 위함.

        while not self.pq.empty():  # queue에 남아 있는 노드가 없으면 끝
            # current_distance, current_destination = heapq.heappop(queue)  # 탐색 할 노드, 거리를 가져옴.
            current_distance, current_destination = self.pq.get()
            if distances[current_destination] < current_distance:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
                continue
            
            for new_destination, new_distance in self.graph[current_destination].items():
                distance = current_distance + new_distance  # 해당 노드를 거쳐 갈 때 거리
                if distance < distances[new_destination]:  # 알고 있는 거리 보다 작으면 갱신
                    distances[new_destination] = distance
                    prev[new_destination] = current_destination
                    self.pq.put((distance, new_destination))
            
        return distances, prev
