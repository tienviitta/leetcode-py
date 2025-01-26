from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key, last=True)
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key, last=True)
        else:
            if len(self.cache) == self.capacity:
                self.cache.popitem(last=False)
            self.cache[key] = value


def test_ex1():
    """
    Input
    ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    Output
    [null, null, null, 1, null, -1, null, -1, 3, 4]

    Explanation
    LRUCache lRUCache = new LRUCache(2);
    lRUCache.put(1, 1); // cache is {1=1}
    lRUCache.put(2, 2); // cache is {1=1, 2=2}
    lRUCache.get(1);    // return 1
    lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    lRUCache.get(2);    // returns -1 (not found)
    lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    lRUCache.get(1);    // return -1 (not found)
    lRUCache.get(3);    // return 3
    lRUCache.get(4);    // return 4
    """
    cmds = [
        ["LRUCache", [2], None],
        ["put", [1, 1], None],
        ["put", [2, 2], None],
        ["get", [1], 1],
        ["put", [3, 3], None],
        ["get", [2], -1],
        ["put", [4, 4], None],
        ["get", [1], -1],
        ["get", [3], 3],
        ["get", [4], 4],
    ]
    s = None
    for cmd in cmds:
        match cmd[0]:
            case "LRUCache":
                s = LRUCache(cmd[1][0])
            case "put":
                res = s.put(cmd[1][0], cmd[1][1])
                assert res == cmd[2]
            case "get":
                res = s.get(cmd[1][0])
                assert res == cmd[2]


if __name__ == "__main__":
    test_ex1()
