# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        rvrs_lst = []
        while curr != None:
            rvrs_lst.append(curr.val)
            curr = curr.next
        rvrs_lst = rvrs_lst[::-1]

        curr = head
        i = 0
        while curr != None:
            curr.val = rvrs_lst[i]
            curr = curr.next
            i+=1

        
        return head
