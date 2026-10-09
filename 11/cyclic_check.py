def is_graph_cyclic(graph):
    visited_overall = set()

    def _is_graph_cyclic(vertex, visited_this_path=None):
        if not visited_this_path:
            visited_this_path = set()

        # already visited while checking this path - found a loop
        if vertex in visited_this_path:
            return True

        # already visited while checking another path - onward paths will be checked there
        if vertex in visited_overall:
            return False

        visited_overall.add(vertex)

        visited_this_path.add(vertex)

        # found a vertex with no onward edges - end of the line for this path
        if vertex not in graph:
            return False

        for next_vertex in graph[vertex]:
            if _is_graph_cyclic(next_vertex, visited_this_path.copy()):
                return True

        # no onward paths found loops
        return False

    for start_vertex in graph:
        if _is_graph_cyclic(start_vertex):
            return True

    return False


links = {}
with open("sample.txt") as f:
    for line in f:
        device, *outputs = line.split()
        device = device.strip(":")
        links[device] = outputs

print(links)
print(is_graph_cyclic(links))
