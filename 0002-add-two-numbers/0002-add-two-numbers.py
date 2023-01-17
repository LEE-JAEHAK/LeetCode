# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        st = ''
        while l1 != None:
            st += str(l1.val)
            l1 = l1.next
        st1 = int(st[::-1])
        st2 = ''
        while l2 != None:
            st2 += str(l2.val)
            l2 = l2.next
        st3 = int(st2[::-1])
        sum = st1 + st3
        string = str(sum)
        head = ListNode(string[-1])
        cur_node = head
        for i in reversed(range(len(string)-1)):
            new_node = ListNode(int(string[i]))
            cur_node.next = new_node
            cur_node = cur_node.next
        return head
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        