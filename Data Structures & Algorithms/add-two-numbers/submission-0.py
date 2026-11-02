# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = num2 = 0
        i = j = 0
        
        curr1 = l1
        while curr1: 
            num1 += curr1.val * (10 ** i)
            i += 1
            curr1 = curr1.next

        curr2 = l2
        while curr2:
            num2 += curr2.val * (10 ** j)
            j += 1
            curr2 = curr2.next
        
        combined = num1 + num2

        dummy = ListNode()
        tmp = dummy
        while combined > 0:
            tmp.next = ListNode(combined % 10)
            combined //= 10
            tmp = tmp.next
        
        return dummy.next if dummy.next else ListNode(0)