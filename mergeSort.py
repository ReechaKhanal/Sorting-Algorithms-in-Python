def startMergeSort(input_array):

	if len(input_array) > 1:

		mid = len(input_array)//2

		left_array = input_array[:mid]
		right_array = input_array[mid:]

		startMergeSort(left_array)
		startMergeSort(right_array)

		i, j, k = 0, 0, 0

		while i < len(left_array) and j < len(right_array):

			if left_array[i] < right_array[j]:
				input_array[k] = left_array[i]
				i = i + 1
			else:
				input_array[k] = right_array[j]
				j = j + 1
			k = k + 1

		while i < len(left_array):
			input_array[k] = left_array[i]
			i = i + 1
			k = k + 1


		while j < len(right_array):
			input_array[k] = right_array[j]
			j = j + 1
			k = k + 1

def mergeSort(input_array):
	startMergeSort(input_array)


if __name__ == '__main__':
	input_array = [4, 56, 2, 1, 43, 5]
	print("Input: " + str(input_array))
	mergeSort(input_array)
	print("Output: " + str(input_array))