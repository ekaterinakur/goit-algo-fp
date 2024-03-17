import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key):
        self.id = str(uuid.uuid4())
        self.val = key
        self.left = None
        self.right = None

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def get_color(order):
    return "#{:06x}".format(0x9400D3 - (order * 10 * 0x020202))

def dfs(node, visited, colors):
    if node is not None:
        visited.add(node.id)
        node_color = get_color(len(visited))
        colors[node.id] = node_color
        if node.left and node.left.id not in visited:
            dfs(node.left, visited, colors)
        if node.right and node.right.id not in visited:
            dfs(node.right, visited, colors)

def bfs(node, colors):
    queue = [node]
    visited = set()
    visited.add(node.id)
    level = 0
    while queue:
        level += 1
        new_queue = []
        for n in queue:
            node_color = get_color(level)
            colors[n.id] = node_color
            if n.left and n.left.id not in visited:
                new_queue.append(n.left)
                visited.add(n.left.id)
            if n.right and n.right.id not in visited:
                new_queue.append(n.right)
                visited.add(n.right.id)
        queue = new_queue

def draw_tree(tree_root, type):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = {}
    if type == "DFS":
        dfs(tree_root, set(), colors)
    elif type == "BFS":
        bfs(tree_root, colors)

    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=[colors[node] for node in tree.nodes()])
    plt.title(f"{type} Traversal")
    plt.show()

def main():
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    draw_tree(root, "DFS")  # Обхід у глибину
    draw_tree(root, "BFS")  # Обхід у ширину

if __name__ == "__main__":
    main()
