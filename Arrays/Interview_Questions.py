# Two Sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

class Solution(object):
    def twoSum(self, nums, target):
        seen = []
        for num in nums:
            if target - num in seen:
                return seen.index(target - num), len(seen)
            else:
                seen.append(nums[0])
                nums = nums[1:]


# Maximum Subarray

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

class Solution(object):
    def maxSubArray(self, nums):
        left = 0
        right = 1
        cur_sum = max_sum = nums[left]
        while right < len(nums):
            if nums[left] < 0:
                left += 1
                right += 1
                cur_sum = nums[left]
                if cur_sum > max_sum:
                    max_sum = cur_sum
            else:
                if cur_sum < 0 and nums[right] > 0:
                    left = right
                    right = left + 1
                    cur_sum = nums[left]
                else:
                    cur_sum += nums[right]
                    right += 1
                if cur_sum > max_sum:
                    max_sum = cur_sum
        return max_sum


# Move Zeroes

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

class Solution(object):
    def moveZeroes(self, nums):
    	zeroes = nums.count(0)
        i = 0
        while zeroes:
            if nums[i] == 0:
                nums.append(nums.pop(i))
                zeroes -= 1
            else:
                i += 1
        return nums


# Contains Duplicates

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution(object):
    def containsDuplicate(self, nums):
        seen = []
        for num in nums:
            if num in seen:
                return True
            else:
                seen.append(num)
        return False


class Solution(object):
    def containsDuplicate(self, nums):
        return not len(set(nums)) == len(nums)


# Rotate Array

# Given an array, rotate the array to the right by k steps, where k is non-negative.

class Solution(object):
	def rotate(self, nums, k):
		k = k % len(nums)
		arr = []
		for i in range(k):
			arr.append(nums.pop())
		nums.reverse()
		nums.extend(arr)
		nums.reverse()
		return nums

class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
