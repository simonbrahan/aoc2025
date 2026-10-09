def count_paths_between(graph, start, end):
    def _count_paths_between(start, end):
        if start == end:
            return 1

        # no onward paths
        if start not in graph:
            return 0

        return sum(_count_paths_between(next, end) for next in graph[start])

    return _count_paths_between(start, end)


graph = {}
with open("input.txt") as f:
    for line in f:
        device, *outputs = line.split()
        device = device.strip(":")
        graph[device] = outputs

print(count_paths_between(graph, "you", "out"))
