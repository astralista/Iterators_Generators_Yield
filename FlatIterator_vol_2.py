class FlatIterator:
    def __init__(self, list_of_list):
        self.stack = list(reversed(list_of_list))

    def __iter__(self):
        return self

    def __next__(self):
        while self.stack:
            try:
                item = self.stack.pop()
                if isinstance(item, list):
                    self.stack.extend(reversed(item))
                else:
                    return item
            except IndexError:
                continue
        raise StopIteration


def test_3():
    list_of_lists_2 = [
        [["a"], ["b", "c"]],
        ["d", "e", [["f"], "h"], False],
        [1, 2, None, [[[[["!"]]]]], []],
    ]

    for flat_iterator_item, check_item in zip(
        FlatIterator(list_of_lists_2),
        ["a", "b", "c", "d", "e", "f", "h", False, 1, 2, None, "!"],
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "h",
        False,
        1,
        2,
        None,
        "!",
    ]


if __name__ == "__main__":
    test_3()
