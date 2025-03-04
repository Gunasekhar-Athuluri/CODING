def merge_sort(arr):
    n = len(arr)
    if n > 1:
        mid = n // 2
        l_arr = arr[:mid]
        r_arr = arr[mid:]

        merge_sort(l_arr)
        merge_sort(r_arr)

        i = j = k = 0

        while i < len(l_arr) or j < len(r_arr):
            if (i < len(l_arr)) and (j >= len(r_arr) or l_arr[i] < r_arr[j]):
                arr[k] = l_arr[i]
                i += 1
            else:
                arr[k] = r_arr[j]
                j += 1
            k += 1


if __name__ == '__main__':
    array = [6, -5, -12, 10, 45, 0, -4, 9, 1]

    merge_sort(array)
    print(str(array))
