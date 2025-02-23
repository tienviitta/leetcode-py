from typing import List, Optional
from icecream import ic


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        stack = []
        stack.append(prerequisites)
        visited = set()
        while stack:
            curr = stack.pop()
            if curr in visited:
                return False
            for neighbor in curr.neighbors:
                stack.append(neighbor)
            visited.add(curr)
        return True


def graphFromAdjList(adjList: List[List[int]]) -> Optional["Node"]:
    nodes = []
    for i in range(len(adjList)):
        nodes.append(Node(i))
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
    """ """
    sol = Solution()
    prereq = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]
    node = graphFromAdjList(prereq)
    res = sol.canFinish(5, node)
    ref = True
    assert res == ref, "res: {}, ref: {}".format(res, ref)


if __name__ == "__main__":
    test_ex1()
