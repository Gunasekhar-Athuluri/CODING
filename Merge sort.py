def mergeSort(array):
    if len(array) > 1:
        # r is the point where the array is divided into two subarrays
        r = len(array) // 2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Merge the two halves
        while i < len(L) or j < len(M):
            if i < len(L) and (j >= len(M) or L[i] < M[j]):
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1


def print_list(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


if __name__ == '__main__':
    array = [6, 5, 12, 10, 45, 0, 4, 9, 1]

    mergeSort(array)

    print("Sorted array is: ")
    print_list(array)
