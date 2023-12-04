# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        dummy = ListNode() ##dummy node
        temp = dummy ## pointer to traverse in dummy node
        while list1 and list2:
            if list1.val<list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        if list1:
            temp.next = list1
            list1 = list1.next
        if list2:
            temp.next = list2
            list2 = list2.next
        return dummy.next
            

if __name__ == "__main__":
    s = Solution()

    list1 = None
    for x in [1,2,4]:
        list1 = ListNode(x, next=list1)

    list2 = None
    for x in [1,3,4]:
        list2 = ListNode(x, next=list2)

    mergeList = s.mergeTwoLists(list1, list2)
    printList = list2
    while printList:
        print(printList.val)
        printList = printList.next
