# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-02-14 00:38:03
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-02-14 00:51:45

# Repeatedly swaps the adjacent elements if they are in wrong order.

def BubbleSort(arr):
	for i in range(len(arr) - 1):
		swapped = False
		for j in range(len(arr) - i - 1):
			if arr[j] > arr[j + 1]:
				# swap arr[j] and arr[j + 1]
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
				swapped = True
		# if there were no swaps in inner loop then break
		if swapped is False:
			break

# Take input from user
A = []
n = input("Enter number of elements in array : ")
print "Enter elements of array : "
for i in range(0, n):
	A.append(input())

print "Input Array : ", A
BubbleSort(A)
print "Sorted Array : ", A