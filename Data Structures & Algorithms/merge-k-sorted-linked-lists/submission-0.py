# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        dummy = ListNode()
        curr = dummy

        while heap:
            val, i, tmp = heapq.heappop(heap)
            curr.next = tmp
            curr = curr.next
            if tmp.next:
                heapq.heappush(heap, (tmp.next.val, i, tmp.next))
        
        return dummy.next