from typing import List

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution():

    def test(self, nums, target):
        if nums is None or len(nums) < 1:
            return []
        dir = {}
        i = 0
        while i<len(nums):
            if dir.get(target - nums[i]) is not None:
                return [i, dir.get(target - nums[i])]
            else:
                dir.update({nums[i]: i})
            i += 1

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.addtt(l1, l2, 0)

    def addtt(self, l1: ListNode, l2: ListNode, k: int) -> ListNode:
        ln = ListNode()
        if l1 is not None and l2 is not None:
            ln.val = (l1.val + l2.val + k)%10
            ln.next = self.addtt(l1.next, l2.next, (l1.val + l2.val + k)//10)
            return ln
        elif l1 is not None and l2 is None:
            ln.val = (l1.val + k)%10
            ln.next = self.addtt(l1.next, None, (l1.val + k)//10)
            return ln
        elif l1 is None and l2 is not None:
            ln.val = (l2.val + k)%10
            ln.next = self.addtt(None, l2.next, (l2.val + k)//10)
            return ln
        elif k is not None and k != 0:
            ln.val = k%10
            return ln
        else:
            return None

    def lengthOfLongestSubstring(self, s: str) -> int:
        lento = 0
        index = 0
        map = {}
        for i in s:
            if map.get(i) is not None:
                value = map.get(i)
                map1 = {}
                for key in map:
                    if map[key] > value:
                        map1.update({key: map[key]})
                map = map1
                map.update({i: index})
            else:
                map.update({i: index})
                if len(map.keys()) > lento:
                    lento = len(map.keys())

            index += 1

        return lento

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        re = 0
        if m == 0 and n == 0:
            return 0
        elif m != 0 and n == 0:
            if m%2 == 0:
                pass
            else:
                pass
        elif m == 0 and n != 0:
            pass
        else:
            pass
        return re





