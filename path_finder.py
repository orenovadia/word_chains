from typing import Optional, Dict, List

from oneedgraph import OneEdGraph


class PathFinder(object):
    def __init__(self, graph: OneEdGraph) -> None:
        super().__init__()
        self._graph = graph

    def shortest_path(self, source, destination) -> Optional[List[str]]:
        if len(source) != len(destination):
            return None

        prev = {source: None}  # type: Dict[str, Optional[str]]

        def record_prev(u, v):
            prev[u] = v
            return u

        level = {source}
        seen = set()
        while level:
            if destination in level:
                break
            seen.update(level)
            level = {record_prev(adjacent, current_word)
                     for current_word in level
                     for adjacent in self._graph.adjacent(current_word)
                     if adjacent not in seen}

        if destination not in prev:
            return None

        path = []
        v = destination
        while v:
            path.append(v)
            v = prev[v]
        path.reverse()
        return path
