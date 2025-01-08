import heapq


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return not self.elements

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

    def __str__(self):
        return str(self.elements)


def test_nops():
    """
    Test normal PriorityQueue operations
    """
    # fmt: off
    cmds = [
        ["PriorityQueue", [None, None], None],
        ["is_empty", [None, None], True],
        ["put", ["eat", 2], None],
        ["put", ["code", 1], None],
        ["put", ["sleep", 3], None],
        ["is_empty", [None, None], False],
        ["get", [None, None], "code"],
        ["get", [None, None], "eat"],
        ["get", [None, None], "sleep"],
        ["is_empty", [None, None], True],
    ]
    # fmt: on
    pq = None
    for cmd in cmds:
        match cmd[0]:
            case "PriorityQueue":
                pq = PriorityQueue()
            case "is_empty":
                res = pq.is_empty()
                assert res == cmd[2]
            case "put":
                pq.put(cmd[1][0], cmd[1][1])
            case "get":
                res = pq.get()
                assert res == cmd[2]


if __name__ == "__main__":
    test_nops()
