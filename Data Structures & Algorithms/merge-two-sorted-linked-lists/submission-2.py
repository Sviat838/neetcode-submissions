# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        cur = res

        while list1 or list2:
            if not list1:
                obj = ListNode(list2.val)
                list2 = list2.next
            elif not list2:
                obj = ListNode(list1.val)
                list1 = list1.next
            elif list1.val <= list2.val:
                obj = ListNode(list1.val)
                list1 = list1.next
            else:
                obj = ListNode(list2.val)
                list2 = list2.next

            cur.next = obj
            cur = obj
        
        return res.next
            

                    