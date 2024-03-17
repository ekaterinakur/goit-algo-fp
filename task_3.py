import heapq

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = {}

    def add_edge(self, start, end, weight):
        self.vertices[start][end] = weight

    def dijkstra(self, source):
        distances = {vertex: float('inf') for vertex in self.vertices}
        previous_vertices = {vertex: None for vertex in self.vertices}
        distances[source] = 0

        priority_queue = [(0, source)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.vertices[current_vertex].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_vertices[neighbor] = current_vertex
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances, previous_vertices

def get_paths(previous_vertices):
    paths = {}

    for vertex, previous_vertex in previous_vertices.items():
        path = []
        current = vertex

        while current is not None:
            path.append(current)
            current = previous_vertices[current]

        path.reverse()
        paths[vertex] = f"{' -> '.join(path)}"
    
    return paths

def main():
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_vertex("E")
    graph.add_edge("A", "B", 4)
    graph.add_edge("A", "C", 2)
    graph.add_edge("B", "C", 5)
    graph.add_edge("B", "D", 10)
    graph.add_edge("C", "D", 3)
    graph.add_edge("C", "E", 8)
    graph.add_edge("D", "E", 6)

    source_vertex = "A"
    distances, previous_vertices = graph.dijkstra(source_vertex)
    paths = get_paths(previous_vertices)

    print('\n')
    print(f"{'-'*42}")
    print("Найкоротша дистанція від ", source_vertex)
    print(f"{'-'*42}")
    print(f"{'Кінцева точка':<15} | {'Дистанція':<10} | {'Шлях':<10}")
    print(f"{'-'*42}")

    for vertex, distance in distances.items():
        print(f"{vertex:<15} | {distance:<10} | {paths[vertex]:<10}")
    
    print('\n')

if __name__ == "__main__":
    main()
