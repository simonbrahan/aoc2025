from functools import cache


def count_paths_between(graph, start, end, must_hit):
    required_hit_count = len(must_hit)

    @cache
    def _count_paths_between(start, end, count_hits):
        if start in must_hit:
            count_hits += 1

        if start == end:
            return count_hits == required_hit_count

        # no onward paths
        if start not in graph:
            return 0

        return sum(_count_paths_between(next, end, count_hits) for next in graph[start])

    return _count_paths_between(start, end, 0)


graph = {}
with open("input.txt") as f:
    for line in f:
        device, *outputs = line.split()
        device = device.strip(":")
        graph[device] = outputs

print(count_paths_between(graph, "svr", "out", set(["fft", "dac"])))
