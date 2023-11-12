# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ref = head
        decimal = 0
        rep = 0
        nums = []
        while (ref != None):
            nums.insert(0, ref.val)
            ref = ref.next

        for n in nums:
            power = 2 ** rep
            value = power * n
            print(value)
            decimal = decimal + value
            rep += 1
        return decimal
