class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


def reverse_string(my_string):
    # Use the "accumulator pattern."
    # Start with an "empty bucket" of the right data type,
    # and build the solution by filling the bucket within a loop.
    reversed_string = ""

    # Create a new stack
    s = Stack()

    # Iterate through my_string and push the characters onto the stack
    for ch in my_string:
        s.push(ch)

    # Use a while loop with the exit condition that the stack is empty.
    # Within this loop, update reversed_string with characters popped off the stack.
    while not s.is_empty():
        reversed_string += s.pop()

    # Return the result
    return reversed_string


def test_nops():
    """
    Test normal Stack operations
    """
    # fmt: off
    cmds = [
        ["Stack", None, None],
        ["is_empty", None, True],
        ["push", 5, None],
        ["push", 3, None],
        ["push", 7, None],
        ["size", None, 3],
        ["is_empty", None, False],
        ["pop", None, 7],
        ["peek", None, 3],
        ["pop", None, 3],
        ["pop", None, 5],
        ["is_empty", None, True],
    ]
    # fmt: on
    s = None
    for cmd in cmds:
        match cmd[0]:
            case "Stack":
                s = Stack()
            case "is_empty":
                res = s.is_empty()
                assert res == cmd[2]
            case "push":
                s.push(cmd[1])
            case "pop":
                res = s.pop()
                assert res == cmd[2]
            case "peek":
                res = s.peek()
                assert res == cmd[2]
            case "size":
                res = s.size()
                assert res == cmd[2]


def test_rev_str():
    test_string = "gninraeL nIdekniL htiw tol a nraeL"
    result_str = reverse_string(test_string)
    assert result_str == "Learn a lot with LinkedIn Learning"


if __name__ == "__main__":
    test_nops()
    test_rev_str()
