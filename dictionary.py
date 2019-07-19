from contextlib import contextmanager
from time import time

from oneedgraph import OneEdGraph
from path_finder import PathFinder


def create_path_finder():
    with open('/usr/share/dict/american-english', encoding='utf8') as f:
        g = OneEdGraph.from_words(f)
    return PathFinder(g)


@contextmanager
def timing(name):
    start = time()
    try:
        yield
    finally:
        print(f'{name} took {time() - start} seconds')


if __name__ == '__main__':
    with timing('build'):
        pf = create_path_finder()

    with timing('search'):
        print(pf.shortest_path('cat', 'dog'))

    with timing('search2'):
        print(pf.shortest_path('lead', 'gold'))

    with timing('search2'):
        print(pf.shortest_path('gold', 'lead'))
