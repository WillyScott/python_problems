
# finded the duplicates
# this problem is from LeetCode
#
testlist = list((1, 2, 3,4))






nums1 = [1, 2, 3, 1]

nums2 = [1, 2, 3, 4]
nums3 = [1,1,1,3,3,4,3,2,4,2]

class Solution(object):
    def containsDuplicates(self, nums):
        """
        :type nums: List(int)
        :rtype: bool

        """
        # create a set with the set constructor which can't have repeating values
        # check length to see

        setlist = set(nums)

        if len(setlist) == len(nums):
            return False
        else:
            return True



sol = Solution()

print(sol.containsDuplicates(nums1))