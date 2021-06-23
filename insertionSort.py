def insertionSort(input_array):

	sorted_index = 0
	curr_index = 0

	while curr_index < len(input_array):
		#print(input_array)
		input_array[curr_index], input_array[sorted_index] = input_array[sorted_index], input_array[curr_index]

		temp = sorted_index
		while (temp-1 >= 0) and (input_array[temp] < input_array[temp-1]):

			input_array[temp], input_array[temp-1] = input_array[temp-1], input_array[temp]
			temp = temp - 1
		
		sorted_index = sorted_index + 1
		curr_index = curr_index + 1

	return input_array

if __name__ == '__main__':
	input_array = [4, 56, 2, 1, 43, 5]
	print("Input: " + str(input_array))
	insertionSort(input_array)
	print("Output: " + str(input_array))