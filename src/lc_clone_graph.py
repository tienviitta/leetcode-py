from typing import List, Optional
from icecream import ic


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraphA(self, node: Optional["Node"]) -> Optional["Node"]:
        oldToNew = {}

        def dfs(node: Optional["Node"]):
            if node in oldToNew:
                return oldToNew[node]
            copy = Node(node.val)
            oldToNew[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy

        return dfs(node) if node else None

    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        stack = []
        stack.append(node)
        visited = set()
        visited.add(node)
        old2new = {}
        while stack:
            old = stack.pop()
            old2new[old] = Node(val=old.val)
            for neighbor in old.neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)
        for old, new in old2new.items():
            for onbr in old.neighbors:
                nnbr = old2new[onbr]
                new.neighbors.append(nnbr)
        return old2new[node]


def graphFromAdjList(adjList: List[List[int]]) -> Optional["Node"]:
    nodes = []
    for i in range(len(adjList)):
        nodes.append(Node(i + 1))
    for i, neighbors in enumerate(adjList):
        for neighbor in neighbors:
            nodes[i].neighbors.append(nodes[neighbor - 1])
    return nodes[0]


def graphToAdjList(node: Optional["Node"]) -> List[List[int]]:
    adjList = []
    stack = []
    stack.append(node)
    visited = set()
    while stack:
        curr = stack.pop()
        if curr in visited:
            continue
        lst = []
        for neighbor in curr.neighbors:
            stack.append(neighbor)
            lst.append(neighbor.val)
        adjList.append(lst)
        visited.add(curr)
    return adjList


def test_ex1():
    """
    Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
    Output: [[2,4],[1,3],[2,4],[1,3]]
    Explanation: There are 4 nodes in the graph.
    1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
    2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
    3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
    4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
    The given node will always be the first node with val = 1. You must return
    the copy of the given node as a reference to the cloned graph.
    """
    sol = Solution()
    adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
    ic(__name__)
    node = graphFromAdjList(adjList)
    out = sol.cloneGraph(node)
    res = graphToAdjList(out)
    ref = [[2, 4], [1, 3], [2, 4], [1, 3]]
    assert res == ref, "res: {}, ref: {}".format(res, ref)


if __name__ == "__main__":
    test_ex1()
