# 2331. Evaluate Boolean Binary Tree

## Problem Link

https://leetcode.com/problems/evaluate-boolean-binary-tree/description/

## Platform

LeetCode

## Difficulty

Easy

## Topic

Tree, DFS, Recursion

## Companies

Not available

## Problem Description

We are given a binary tree.

Each leaf node has value:

    0 -> False
    1 -> True

Each internal node has value:

    2 -> OR
    3 -> AND

We need to evaluate the whole tree and return final boolean answer.

## Intuition

This is a DFS recursion problem.

Every subtree will return one boolean value.

Leaf node directly gives True or False.

Internal node combines left subtree answer and right subtree answer.

If current node value is 2:

    return left OR right

If current node value is 3:

    return left AND right

## State Meaning

    dfs(root)

means:

    return the boolean value of this subtree

## DFS Logic

First handle leaf node.

If node is leaf:

    value 1 means True
    value 0 means False

For internal node:

    left = dfs(root.left)
    right = dfs(root.right)

Then apply operator.

If root.val == 2:

    left or right

If root.val == 3:

    left and right

## Code

    from typing import Optional

    class Solution:
        def dfs(self, root):
            if root.left is None and root.right is None:
                if root.val == 1:
                    return True
                else:
                    return False

            left = self.dfs(root.left)
            right = self.dfs(root.right)

            if root.val == 2:
                return left or right
            else:
                return left and right

        def evaluateTree(self, root: Optional[TreeNode]) -> bool:
            return self.dfs(root)

## Dry Run

Example tree:

            2
           / \
          1   3
             / \
            0   1

Meaning:

    2 = OR
    3 = AND
    1 = True
    0 = False

So expression becomes:

    True OR (False AND True)

Start from root:

    dfs(2)

Node 2 is OR, so we need:

    dfs(left) or dfs(right)

Left child is 1.

    dfs(1) = True

Right child is 3.

Node 3 is AND, so:

    dfs(0) and dfs(1)

Leaf 0 gives:

    False

Leaf 1 gives:

    True

So node 3 gives:

    False and True = False

Now root node 2 gives:

    True or False = True

Final answer:

    True

## Why Return Is Important

This problem is not about storing path.

Every recursive call gives one answer back to its parent.

Example:

    dfs(0) returns False
    dfs(1) returns True

Then parent node uses those returned values.

For OR node:

    return left or right

For AND node:

    return left and right

## Common Mistake

Wrong:

    self.dfs(root.left)
    self.dfs(root.right)

This only calls DFS but does not use the result.

Correct:

    left = self.dfs(root.left)
    right = self.dfs(root.right)

Because we need left and right boolean answers.

## Complexity

Let:

    n = number of nodes

Time Complexity:

    O(n)

Because every node is visited once.

Space Complexity:

    O(h)

Where h is height of tree due to recursion stack.

In worst case:

    O(n)

In balanced tree:

    O(log n)

## Key Learning

Whenever a tree problem says:

    evaluate expression tree
    leaf gives value
    internal node gives operation

Think:

    DFS recursion + return value from left and right subtree
