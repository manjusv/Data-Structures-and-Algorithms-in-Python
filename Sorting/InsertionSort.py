# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-02-08 18:41:57
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-02-08 19:21:23

""" Insertion sort works the way we sort playing cards """

class insertionsort:
	def InsertionSort(self, arr):
		for i in range(1, len(arr)):
			key = arr[i]
			j = i - 1

			# move elements from index 0 to i - 1 if greater than key
			while j >= 0 and arr[j] > key:
				arr[j + 1] = arr[j]
				j -= 1
			# put key to correct position
			arr[j + 1] = key

# create an obj of class
obj = insertionsort()

# Take input from user
A = []
n = input("Enter number of elements in array : ")
print "Enter elements of array : "
for i in range(0, n):
	A.append(input())

print "Input Array : ", A
obj.InsertionSort(A)
print "Sorted Array : ", A