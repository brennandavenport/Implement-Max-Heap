def test_pop_empty_returns_none(heap_cls):
    heap = heap_cls()

    assert heap.pop() is None, "expected popping an empty heap to return None"
