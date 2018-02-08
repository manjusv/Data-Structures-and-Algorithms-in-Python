# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-02-08 19:30:55
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-02-08 19:39:19

"""Picks the minimum element from unsorted array and puts at begining"""

def SelectionSort(arr):
	for i in range(0, len(arr) - 1):
		min_index = i
		# find minimum element from unsorted array
		for j in range(i + 1, len(arr)):
			if arr[j] < arr[min_index]:
				min_index = j

		# put minimum element to begining of unsorted array
		arr[i], arr[min_index] = arr[min_index], arr[i]

# Take input from user
A = []
n = input("Enter number of elements in array : ")
print "Enter elements of array : "
for i in range(0, n):
	A.append(input())

print "Input Array : ", A
SelectionSort(A)
print "Sorted Array : ", A