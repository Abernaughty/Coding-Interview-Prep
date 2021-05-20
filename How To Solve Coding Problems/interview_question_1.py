import time


def timer(func):
	def wrapper(*args):
		start_time = time.time()
		res = func(*args)
		print(f'time to run {func.__name__}: ', (time.time() - start_time) * 100, 'ms')
		return res
	return wrapper


# Given 2 arrays, create a function that lets a user know the (true/false) whether these two arrays contain any common items.

# arr1 = ['a', 'b', 'c', 'x']
# arr2 = ['z', 'y', 'i']
# arr3 = ['a', 'b', 'c', 'x']
# arr4 = ['z', 'y', 'x']
arr1 = [n for n in range(10000)]
arr2 = [n for n in range(10000, 20000)]
arr3 = [n for n in range(20000, 30000)]
arr4 = [n for n in range(30000, 40000)]


# Brute Force
@timer
def array_intersect1(arr1, arr2):
	# set longer array as primary and shorter as secondary
	if len(arr1) >= len(arr2):
		p_arr = arr1
		s_arr = arr2
	else:
		p_arr = arr2
		s_arr = arr1

	# check if any val in primary arr is in secondary arr
	for val in p_arr:
		if val in s_arr:
			return True
	return False

@timer
def array_intersect2(arr1, arr2):
	arr_1 = set(arr1)

	for item in arr2:
		if item in arr_1:
			return True
	return False

@timer
def smarter_matching2(array1, array2):
    try:
        dictionary = dict()
        for i in range(len(array1)):
            if array1[i] not in dictionary:
                dictionary[array1[i]] = True

        for i in range(len(array2)):
            if array2[i] in dictionary:
                return True
        return False

    except TypeError:
        return "Exactly two arrays required."

print(array_intersect2(arr1, arr2))
print(smarter_matching2(arr1, arr2))
print(array_intersect2(arr3, arr4))
print(smarter_matching2(arr3, arr4))