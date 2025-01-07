from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        # Add from the right hand side
        self.items.append(item)

    def dequeue(self):
        # Remove from the left hand side
        return self.items.popleft()

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


def test_nops():
    """
    Test normal Stack operations
    """
    # fmt: off
    cmds = [
        ["Queue", None, None],
        ["is_empty", None, True],
        ["enqueue", 5, None],
        ["enqueue", 3, None],
        ["enqueue", 7, None],
        ["size", None, 3],
        ["is_empty", None, False],
        ["dequeue", None, 5],
        ["peek", None, 3],
        ["dequeue", None, 3],
        ["dequeue", None, 7],
        ["is_empty", None, True],
    ]
    # fmt: on
    s = None
    for cmd in cmds:
        match cmd[0]:
            case "Queue":
                s = Queue()
            case "is_empty":
                res = s.is_empty()
                assert res == cmd[2]
            case "enqueue":
                s.enqueue(cmd[1])
            case "dequeue":
                res = s.dequeue()
                assert res == cmd[2]
            case "peek":
                res = s.peek()
                assert res == cmd[2]
            case "size":
                res = s.size()
                assert res == cmd[2]


if __name__ == "__main__":
    test_nops()
