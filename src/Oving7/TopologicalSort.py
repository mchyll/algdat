from Graph import GraphNode, Graph, import_graph


def df_topo(node: GraphNode, node_list: GraphNode):
    if node.found:
        return node_list

    node.found = True
    for neighbor in node.get_neighbors():
        node_list = df_topo(neighbor, node_list)

    node.next_node = node_list
    return node


def topological_sort(graph: Graph):
    # Reset nodes
    for node in graph.nodes:
        node.found = False
        node.next_node = None

    node_list: GraphNode = None
    for node in graph.nodes:
        node_list = df_topo(node, node_list)

    return node_list


if __name__ == "__main__":
    graph = import_graph("L7g5")

    print("Running topological sort")
    node_list = topological_sort(graph)

    while node_list is not None:
        print("{} -> ".format(node_list.label), end='')
        node_list = node_list.next_node
