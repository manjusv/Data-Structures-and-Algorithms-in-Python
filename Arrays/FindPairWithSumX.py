# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-01-08 19:48:04
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-01-11 16:26:40

# Given an array A and a number x, check for pair in A with sum as x

class Solution():
	# Function to find the partiioning index
	def Partition(self, A, low, high):
		pivot = A[high]

		i = (low - 1)
		for j in range(low, high):
			if A[j] <= pivot:
				i += 1
				# swap A[i] and A[j]
				A[i], A[j] = A[j], A[i]

		# swap A[i + 1] and A[high]
		A[i + 1], A[high] = A[high], A[i + 1]

		return (i + 1)


	# Function to sort the array in non-decreasing order
	# we can go for any sorting method, here i will use quicksort
	def quickSort(self, A, low, high):
		if low < high:
			# pi is the partitioning index, A[pi] will be at correct place
			pi = self.Partition(A, low, high)

			# recursively call quickSort for 2 halfs
			self.quickSort(A, low, pi - 1)
			self.quickSort(A, pi + 1, high)

	# Function to check if there exists a pair with sum X
	def FindPair(self, A, X):
		i = 0
		j = len(A) - 1
		while i < j:
			# if equal to sum return
			if A[i] + A[j] == X:
				return True
			# if sum is less than given sum
			elif A[i] + A[j] < X:
				i += 1
			else:
				j -= 1

		# will reach here only when we didn't get a pair
		return False

# create an obj of the class
obj = Solution()

A = [1,1,1,11,2,3,5,6,29,2,3,4]
X = 40

print "Input Array : ", A
print "Given Sum : ", X

# sort the array in non descending order
obj.quickSort(A, 0, len(A) - 1)

print "Sorted Array : " , A
if obj.FindPair(A, X):
	print "There exists a pair with sum X"
else:
	print "There is no pair with sum X"