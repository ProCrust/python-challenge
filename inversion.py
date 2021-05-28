"""
	Counting Inversion
	#Counting Inversion traverses through a given list then counts the inversion in the list
	#	a pair(x,y) is considered inversion when index(x) < index(y) but value(x) > value(y)
	#This algorithm uses Divide and Conquer recursive-approach,
	#	specifically a modified Merge-And-Conquer algorithm
	#invCount() is the modified Merge-and-Conquer algorithm which accepts a list of element
	#	then returns the sorted version of the list as well as the number of inversion that is in the list
	#force() is the brute-force algorithm to solve the inversion problem
	#use inv_input for one test-case input
	#use inv_test for multiple test-case input


	#Kent Joash A. Zamudio
	#CMSC 142 (lab) - Exercise 3
"""

#invCount() divides the list by half (Left and Right) then process each list
def invCount(arr):

	count = 0 #inversion count
	arrSort = list() #a sorted version of the list in the argument

	if len(arr) == 1: #if there is only 1 element in the list
		return arr, 0	#simply return the list and 0 since it is impossible to have a pair(x,y)
	else:
		midInd = len(arr)/2 #getting the middle index of the list
		LEFT = arr[:midInd] #copying the left part of the original list (from zero to middle index-1)
		RIGHT = arr[midInd:] #copying the right part of the original list (from middle index to last index)

		#sends each part to invCount()
		LEFT, invL = invCount(LEFT)
		RIGHT, invR = invCount(RIGHT)

		#the resulting inversion count from each side is the summed up
		count = invL + invR 

		#this part is where inversions are counted
		leftInd = rightInd = 0

		while len(LEFT) > leftInd and len(RIGHT) > rightInd:


			#if leftItem < rightItem, no increment in count since right elements should be greater
			if LEFT[leftInd] <= RIGHT[rightInd]:
				arrSort.append(LEFT[leftInd])
				leftInd+=1

			elif LEFT[leftInd] > RIGHT[rightInd]:	#otherwise, there is an inversion.
				arrSort.append(RIGHT[rightInd])
				rightInd+=1

				#if we only increment 1 in the 'count', it will result to a wrong number of inversions
				# 	because in the later part of the recursion the processed list is already sorted
				#	by subtracting the index to the length of the LEFT list,
				#	the jumps of the elements is taken into consideration
				#	uncomment the print statement to see jumps of element due to sorting
				count+= (len(LEFT)-leftInd)
				# print "jumps:", len(LEFT)-leftInd, "latest count:", count
				
		#if there are elements left in the left list, we copy those elements to the sorted list
		arrSort+= LEFT[leftInd:]	
		arrSort+= RIGHT[rightInd:]

	return arrSort, count


def force(arr):		#brute force algorithm
	counterrr = 0
	for item in arr:
		arr2 = arr[arr.index(item)+1:]
		for iterate in arr2:
			if item > iterate:
				counterrr+=1
	print 'Brute Force Result: ',counterrr
	
def main():
	global count
	cases = int(raw_input())
	for thisTest in range(cases):
		arr = [int(x) for x in raw_input().strip().split()]

		#for terminal use
		# print '====================================='
		# sortedArr, count = invCount(arr)
		print 'input  ', arr
		# print 'sorted ', sortedArr
		# force(arr)
		# print 'Divide and Conquer Result: ', count

		#for file use
		sortedArr, count = invCount(arr)
		print count

main()