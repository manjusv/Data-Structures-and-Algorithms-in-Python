# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-02-08 17:06:39
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-04-06 18:27:53

""" QuickSort is a divide and conquer algorithm. It picks an element
as pivot and partitions the array around it. Here we use last element of
array as pivot"""


class quicksort:
    def QuickSort(self, arr, low, high):
        """ Sorts the given array using divide and conquer method"""
        if low < high:
            p_index = self.Partition(arr, low, high)

            # Now arr[p_index] is at correct position
            # call QuickSort recursivery
            self.QuickSort(arr, low, p_index - 1)
            self.QuickSort(arr, p_index + 1, high)

    def Partition(self, arr, low, high):
        # consider last element as pivot
        pivot = arr[high]
        # i tracks elements smaller than pivot
        i = low - 1

        for j in range(low, high):
            if arr[j] <= pivot:
                # increment index of smaller element
                i = i + 1
                # swap arr[i] and arr[j]
                arr[i], arr[j] = arr[j], arr[i]

        # Now i + 1 is the correct index of pivot after sorting
        # so swap arr[i + 1] and pivot
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return (i + 1)


# create an obj of class
obj = quicksort()

# Take input from user
A = []
n = input("Enter number of elements in array : ")
print "Enter elements of array : "
for i in range(0, n):
    A.append(input())

print "Input Array : ", A
obj.QuickSort(A, 0, len(A) - 1)
print "Sorted Array : ", A
