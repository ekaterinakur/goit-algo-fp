import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="violet"):
        self.id = f'Node_{key}'
        self.val = key
        self.color = color
        self.left = None
        self.right = None

class Heap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        heapq.heappush(self.heap, value)

    def pop(self):
        return heapq.heappop(self.heap)

    def add_edges(self, graph, node, pos, x=0, y=0, layer=1):
        if node is not None:
            graph.add_node(node.id, color=node.color, label=node.val)
            if node.left:
                graph.add_edge(node.id, node.left.id)
                l = x - 1 / 2 ** layer
                pos[node.left.id] = (l, y - 1)
                l = self.add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
            if node.right:
                graph.add_edge(node.id, node.right.id)
                r = x + 1 / 2 ** layer
                pos[node.right.id] = (r, y - 1)
                r = self.add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
        return graph

    def build_heap_tree(self, index=0):
        if index >= len(self.heap):
            return None

        node = Node(self.heap[index])

        left_index = 2 * index + 1
        right_index = 2 * index + 2
        node.left = self.build_heap_tree(left_index)
        node.right = self.build_heap_tree(right_index)

        return node

    def draw_tree(self, tree_root):
        tree = nx.DiGraph()
        pos = {tree_root.id: (0, 0)}
        tree = self.add_edges(tree, tree_root, pos)

        colors = [node[1]['color'] for node in tree.nodes(data=True)]
        labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

        plt.figure(figsize=(8, 5))
        nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
        plt.show()

def main():
    heap = Heap()
    
    for value in [10, 5, 7, 3, 12, 8]:
        heap.insert(value)
        
    heap_tree_root = heap.build_heap_tree()
    heap.draw_tree(heap_tree_root)

if __name__ == "__main__":
    main()
