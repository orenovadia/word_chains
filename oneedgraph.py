from collections import defaultdict
from typing import Set, Dict


class OneEdGraph:
    def __init__(self) -> None:
        super().__init__()
        # groups of words that are 1 ed grouped by
        # The same word with that character replaced with '?'
        # e.g: c?t -> {cat, cot}
        self._groups = defaultdict(set)  # type: Dict[str, Set[str]]

    @classmethod
    def from_words(cls, words):
        g = OneEdGraph()
        for word in words:
            g.add_word(word)
        return g

    def add_word(self, word):
        word = normalize(word)
        for key in self._keys(word):
            self._groups[key].add(word)

    def adjacent(self, word):
        word = normalize(word)
        return {adj
                for key in self._keys(word)
                for adj in self._groups.get(key, ())
                if adj is not word}

    def _keys(self, word):
        return [word[:i] + '?' + word[i + 1:]
                for i in range(len(word))]


def normalize(word):
    return word.strip().lower()


if __name__ == '__main__':
    print(OneEdGraph.from_words(['cat', 'cot', 'dog', 'cog']).adjacent('cog'))
