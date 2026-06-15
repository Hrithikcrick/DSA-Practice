# 2095. Delete the Middle Node of a Linked List

## Problem Link

https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/

## Platform

LeetCode

## Difficulty

Medium

## Topic

Linked List, Slow and Fast Pointer

## Companies

Not available

## Problem Description

You are given the head of a linked list.

Delete the middle node and return the head of the modified linked list.

## Intuition

We need to delete the middle node.

In linked list, we cannot directly access index like an array.

So we use slow and fast pointers.

Slow pointer moves one step.

Fast pointer moves two steps.

When fast reaches the end, slow reaches the middle node.

But to delete slow, we also need the previous node.

So we maintain prev.

Then delete slow using:

    prev.next = slow.next

## Code

    from typing import Optional

    class Solution:
        def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
            if head.next is None:
                return None

            slow = head
            fast = head
            prev = None

            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next

            prev.next = slow.next

            return head

## Dry Run

Input:

    head = [1, 3, 4, 7, 1, 2, 6]

Linked list:

    1 -> 3 -> 4 -> 7 -> 1 -> 2 -> 6

Initial:

    slow = 1
    fast = 1
    prev = None

First loop:

    prev = 1
    slow = 3
    fast = 4

Second loop:

    prev = 3
    slow = 4
    fast = 1

Third loop:

    prev = 4
    slow = 7
    fast = 6

Now fast.next is None, so loop stops.

Middle node is:

    slow = 7

Delete it:

    prev.next = slow.next

So:

    4.next = 1

Final list:

    1 -> 3 -> 4 -> 1 -> 2 -> 6

## Edge Case

If linked list has only one node:

    head = [1]

Return:

    None

## Complexity

Time Complexity: O(n)

Space Complexity: O(1)
