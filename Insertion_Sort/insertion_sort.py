def insertionSort(array):

	for i in range(1, len(array)):

		temp = i
		while (temp-1 >= 0) and (array[temp] < array[temp-1]):
			array[temp], array[temp-1] = array[temp-1], array[temp]
			temp = temp - 1

	return array