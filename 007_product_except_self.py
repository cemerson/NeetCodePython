# 007_product_except_self.py

class Solution007:
    """
    Given an integer list nums, return a list output where output[i] is the product of all the elements
    of nums except nums[i].
    """
    def product_except_self(self, nums):
        # Solution goes here
        return nums

    # test method, consistent in every file
    def test(self):
        test_cases = [
            [1, 2, 4, 6],
            [-1, 0, 1, 2, 3]
        ]
        for nums in test_cases:
            result = self.product_except_self(nums)
            print(f"Input: {nums} Output: {result}")
