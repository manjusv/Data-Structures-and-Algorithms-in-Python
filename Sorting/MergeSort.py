# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-02-08 17:54:15
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-02-08 18:37:14

""" MergeSort is also a divide and conquer algorithm. It divides the input array
into two halves and calls itself for two halves and merges the two sorted arrays """

class mergesort:
	def MergeSort(self, arr, low, high):
		""" Sorts the given array using divide and conquer method"""
		if low < high:
			mid = low + (high - low) / 2

			self.MergeSort(arr, low, mid)
			self.MergeSort(arr, mid + 1, high)
			self.merge(arr, low, mid, high)

	def merge(self, arr, low, mid, high):
		nrof_elements_first_half = mid - low + 1
		nrof_elements_second_half = high - mid

		# create temporary arrays
		L = []
		R = []

		# copy elements to temp arrays
		for i in range(0, nrof_elements_first_half):
			L.append(arr[low + i])

		for j in range(0, nrof_elements_second_half):
			R.append(arr[mid + 1 + j])

		# merge the temp arrays
		i, j, k = 0, 0, low

		while i < nrof_elements_first_half and j < nrof_elements_second_half:
			if L[i] <= R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		# copy remaining elements from L if any
		while i < nrof_elements_first_half:
			arr[k] = L[i]
			i += 1
			k += 1

		# copy remaining elements from R if any
		while j < nrof_elements_second_half:
			arr[k] = R[j]
			j += 1
			k += 1

# create an obj of class
obj = mergesort()

# Take input from user
A = []
n = input("Enter number of elements in array : ")
print "Enter elements of array : "
for i in range(0, n):
	A.append(input())

print "Input Array : ", A
obj.MergeSort(A, 0, len(A) - 1)
print "Sorted Array : ", A