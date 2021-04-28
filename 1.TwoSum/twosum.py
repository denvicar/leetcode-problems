"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""


def twoSum(nums, target):
    result = []
    i = 0
    while len(result) == 0:
        a = nums[i]
        b = [(index, value) for index, value in enumerate(nums) if value + a == target][0][0]
        if b:
            result = [i, b]
        else:
            i = i + 1
    return result
