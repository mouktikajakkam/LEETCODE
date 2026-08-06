from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Dictionary (HashMap) to store:
        # key   -> number in the array
        # value -> index of that number
        #
        # Example:
        # {2: 0, 7: 1}
        prevMap = {}

        # enumerate(nums) gives both:
        # i -> current index
        # n -> current number
        #
        # Example:
        # nums = [2, 7, 11, 15]
        #
        # Iteration 1: i = 0, n = 2
        # Iteration 2: i = 1, n = 7
        # Iteration 3: i = 2, n = 11
        # Iteration 4: i = 3, n = 15
        for i, n in enumerate(nums):

            # Find the number needed to reach the target.
            #
            # Example:
            # target = 9
            # n = 7
            #
            # diff = 9 - 7 = 2
            diff = target - n

            # Check whether the required number (diff)
            # has already been seen.
            #
            # Example:
            # prevMap = {2: 0}
            # diff = 2
            #
            # Since 2 exists in prevMap,
            # we have found the answer.
            if diff in prevMap:

                # Return:
                # Index of the previous number
                # Current index
                #
                # Example:
                # return [0, 1]
                return [prevMap[diff], i]

            # If the required number wasn't found,
            # store the current number and its index.
            #
            # Example:
            # n = 2
            # i = 0
            #
            # prevMap becomes:
            # {2: 0}
            prevMap[n] = i

        # According to the LeetCode problem,
        # there is always exactly one solution,
        # so this line is usually never executed.
        return []