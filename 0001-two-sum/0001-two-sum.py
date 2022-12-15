class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # implement a HashMap or some kind of dictionary to hold key, value paris.
        pair_d = {}

        # Loop to iterate through the array
        for i,num in enumerate(nums):
            # conditional check to see if the number exists inside the dictionary.
            if num in pair_d: return pair_d[num], i
            # if it doesn't exist, sub the target value from num to get the second value and add it to the dictionary.
            pair_d[target-num]=i
            