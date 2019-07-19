from unittest import TestCase

from oneedgraph import OneEdGraph
from path_finder import PathFinder


class Tests(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.g = OneEdGraph.from_words(['cat', 'dog', 'cot', 'cog'])
        cls.paths = PathFinder(cls.g)

    def test_shortest_path(self):
        path = self.paths.shortest_path('cat', 'dog')
        self.assertEqual(['cat', 'cot', 'cog', 'dog'], path)

    def test_no_shortest_path(self):
        path = self.paths.shortest_path('hay', 'dog')
        self.assertIsNone(path)
