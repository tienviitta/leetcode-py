from src.pdsa_stack import Stack


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
