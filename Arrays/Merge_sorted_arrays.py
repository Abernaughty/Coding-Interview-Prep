# def mergeSortedArrays(*args):
# 	arr = []
# 	for array in args:
# 		arr += array
# 	return sorted(arr)

def mergeSortedArrays(arr_1, arr_2):
	merged_array = []
	while arr_1 and arr_2:
		if arr_1[0] < arr_2[0]:
			merged_array.append(arr_1.pop(0))
		elif arr_1[0] > arr_2[0]:
			merged_array.append(arr_2.pop(0))
		elif arr_1[0] == arr_2[0]:
			merged_array.append(arr_1.pop(0))
			merged_array.append(arr_2.pop(0))
	if arr_1 and not arr_2:
		merged_array += arr_1
	elif arr_2 and not arr_1:
		merged_array += arr_2
	return merged_array

print(mergeSortedArrays([1, 3, 4, 31], [4, 6, 30]))