from src.pdsa_stack import Stack


def test_normal():
    """
    Test normal Stack operations
    """
    cmds = [
        ["Stack", None, None],
        ["is-empty", None, True],
        ["push", 5, None],
        ["push", 3, None],
        ["push", 7, None],
        ["size", None, 3],
        ["is-empty", None, False],
        ["pop", None, 7],
        ["peek", None, 3],
        ["pop", None, 3],
        ["pop", None, 5],
        ["is-empty", None, True],
    ]
    s = None
    for cmd in cmds:
        match cmd[0]:
            case "Stack":
                s = Stack()
            case "is_empty":
                res = s.is_empty()
                assert res == cmd[2]
