import time
import random

# arr1 = [1, 2, 3, 9]
# arr2 = [1, 2, 4, 4]
big_arr = sorted([random.randint(1, 1000) for _ in range(5000)])
sum = 1000

def timer(func):
	def wrapper(*args):
		start_time = time.time()
		res = func(*args)
		print(f'time to run {func.__name__}: ', (time.time() - start_time) * 100, 'ms')
		return res
	return wrapper

## Brute Force
# @timer
# def has_pair_with_sum(arr, sum):
# 	for num in arr:
# 		if num > sum:
# 			break
# 		if sum - num in arr:
# 			return num, sum - num
# 	return 'No pair exists.'

## Binary Search
# @timer
# def has_pair_with_sum(arr, sum):
# 	for i in range(len(arr)):
# 		if arr[i] > sum:
# 			break
# 		if sum - arr[i] > sum:
# 			continue
# 		compliment = sum - arr[i]
# 		search_arr = arr[i:]
# 		match = bin_search_recursive(search_arr, compliment, 0, len(search_arr) - 1)
# 		if match:
# 			return arr[i], match
# 	return 'No pair exists.'

# def bin_search_recursive(array, element, start, end):
#     if start > end:
#         return 0

#     mid = (start + end) // 2
#     if element == array[mid]:
#         return array[mid]

#     if element < array[mid]:
#         return bin_search_recursive(array, element, start, mid-1)
#     else:
#         return bin_search_recursive(array, element, mid+1, end)

## Search from outside in
# @timer
# def has_pair_with_sum(arr, sum):
# 	"""

# 	Searches through array of integers for 
# 	two integers that add up to the provided sum.

# 	"""

# 	# set starting upper and lower bound
# 	low = 0
# 	high = len(arr) - 1

# 	# test if upper + lower = sum
# 	while low < high:

# 		# if upper + lower = sum, return both numbers
# 		if arr[low] + arr[high] == sum:
# 			return arr[low], arr[high]

# 		# if upper + lower > sum, move upper bound left
# 		elif arr[low] + arr[high] > sum:
# 			high -= 1

# 		# if upper + lower < sum, move lower bound right
# 		elif arr[low] + arr[high] < sum:
# 			low += 1

# 	return 'No pairs found.'

@timer
def has_pair_with_sum1(arr, sum):
	seen = set()
	for num in arr:
		if sum - num in seen:
			return num, sum - num
		seen.add(num)
	return 'No pairs found.'


@timer
def has_pair_with_sum2(arr, sum):
	seen = set()
	for num in arr:
		if num in seen:
			return num, sum - num
		seen.add(sum - num)
	return 'No pairs found.'


# print(pair_sum1(big_arr, sum))
# print(pair_sum2(big_arr, sum))
# print(pair_sum3.__doc__)
# print(help(pair_sum3))
print(has_pair_with_sum1(big_arr, 1000))
print(has_pair_with_sum2(big_arr, 1000))
print(has_pair_with_sum1(big_arr, 10000))
print(has_pair_with_sum2(big_arr, 10000))
