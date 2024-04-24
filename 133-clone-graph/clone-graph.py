"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}
        
        def dfs_clone(node):
            # if node is already in table, return the new version of that node
            if node in oldToNew:
                return oldToNew[node]
            
            # create a copy of the current node
            copy = Node(node.val)
            # add the copy to the table, with the current node mapping to the copy
            oldToNew[node] = copy

            # "recursive" call - for each of the neighbors for the current node,
            # copy its neighbors and add it to copy's neighbors list
            for n in node.neighbors:
                copy.neighbors.append(dfs_clone(n))
            
            return copy
        
        # return the returning graph of the function if node is not NULL
        return dfs_clone(node) if node else None
