# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        if mountain_arr.length() < 3:
            return -1


        
        ans = -1
        left = 1
        right = mountain_arr.length() - 2
        

        while left <= right:
            mid = left + (right - left) // 2
            m_val = mountain_arr.get(mid)
            r_val = mountain_arr.get(mid + 1)
            l_val = mountain_arr.get(mid - 1)

            if l_val < m_val and m_val > r_val:
               peak = mid
               break

            elif l_val < m_val:
                left = mid + 1
            else:
                right = mid - 1

        left = 0
        right = peak

        while left <= right:
            mid = left + (right - left) // 2
            m_val = mountain_arr.get(mid)

            if m_val == target:
                return mid
            elif m_val > target:
                right = mid - 1
            else:
                left = mid + 1

        left = peak
        right = mountain_arr.length() - 1

        while left <= right:
            mid = left + (right - left) // 2
            m_val = mountain_arr.get(mid)

            if m_val == target:
                return mid
            elif m_val > target:
                left = mid + 1
            else:
                right = mid - 1

        return ans