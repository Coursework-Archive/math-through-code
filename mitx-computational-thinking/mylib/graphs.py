# mylib/graphs.py

class Node(object):
    def __init__(self, name):
        """
        :param name: a string
        """
        self.name = name

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name

    __repr__ = __str__


class Edge(object):
    def __init__(self, src, dest):
        """
        :param src: Node
        :param dest: Node
        """
        self._src = src
        self._dest = dest

    def get_source(self):
        return self._src

    def get_destination(self):
        return self._dest

    def __str__(self):
        return self._src.get_name() + " -> " + self._dest.get_name()


class Weighted_Edge(Edge):
    def __init__(self, src, dest, weight=1.0):
        """
        :param src: Node
        :param dest: Node
        :param weight: a number
        """
        # use parent init for src/dest
        super().__init__(src, dest)
        self._weight = weight

    def get_weight(self):
        return self._weight

    def __str__(self):
        return (self._src.get_name()
                + " -> " + self._dest.get_name()
                + " weight: " + str(self._weight))


class Digraph(object):
    """
    nodes is a list of the nodes in the graph
    edges is a dict mapping each node to a list of its children
    """
    def __init__(self):
        self._nodes = []
        self._edges = {}

    def add_node(self, node):
        if node in self._nodes:
            raise ValueError("Node already exists")
        self._nodes.append(node)
        self._edges[node] = []

    def add_edge(self, edge):
        src = edge.get_source()
        dest = edge.get_destination()
        if src not in self._nodes or dest not in self._nodes:
            raise ValueError("Node does not exist")
        self._edges[src].append(dest)

    def children_of(self, node):
        return self._edges[node]

    def has_node(self, node):
        return node in self._nodes

    def __str__(self):
        result = ''
        for src in self._nodes:
            for dest in self._edges[src]:
                result += src.get_name() + " -> " + dest.get_name() + '\n'
        return result[:-1]  # omit final newline

    def get_edges(self):
        result = []
        for src in self._edges:
            for dest in self._edges[src]:
                result.append((src, dest))
        return result


class Graph(Digraph):

    def add_edge(self, edge):
        # add original direction
        super().add_edge(edge)
        # add reverse direction
        rev = Edge(edge.get_destination(), edge.get_source())
        super().add_edge(rev)


def print_path(path):
    """
    :param path: a list of nodes
    :return: string
    """
    return '->'.join(str(node) for node in path)


def DFS(graph, start, end, path, shortest, to_print=False):
    """
    :param graph: Digraph
    :param start: Node
    :param end: Node
    :param path: list of Nodes
    :param shortest: shortest list of Nodes
    :param to_print: bool
    :return: shortest path from start to end
    """
    path = path + [start]
    if to_print:
        print("Current DFS path:", print_path(path))
    if start == end:
        return path
    for node in graph.children_of(start):
        if node not in path:  # avoid cycles
            if shortest is None or len(path) < len(shortest):
                new_path = DFS(graph, node, end, path, shortest, to_print)
                if new_path is not None:
                    shortest = new_path
    return shortest


def shortest_path(graph, start, end, to_print=False):
    """
    :param graph: Digraph
    :param start: Node
    :param end: Node
    :param to_print: bool
    :return: shortest path from start to end
    """
    return DFS(graph, start, end, [], None, to_print)


def test_SP():
    nodes = []
    for name in range(6):   # create 6 nodes "0"..."5"
        nodes.append(Node(str(name)))

    g = Digraph()
    for n in nodes:
        g.add_node(n)

    g.add_edge(Edge(nodes[0], nodes[1]))
    g.add_edge(Edge(nodes[1], nodes[2]))
    g.add_edge(Edge(nodes[2], nodes[3]))
    g.add_edge(Edge(nodes[2], nodes[4]))
    g.add_edge(Edge(nodes[3], nodes[4]))
    g.add_edge(Edge(nodes[3], nodes[5]))
    g.add_edge(Edge(nodes[0], nodes[2]))
    g.add_edge(Edge(nodes[1], nodes[0]))
    g.add_edge(Edge(nodes[3], nodes[1]))
    g.add_edge(Edge(nodes[4], nodes[0]))

    sp = shortest_path(g, nodes[0], nodes[5], to_print=True)
    print('Shortest path found by DFS:', print_path(sp))
