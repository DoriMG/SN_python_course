def bad_sort(list_to_sort):
    sorted_list = []
    for i,el in enumerate(list_to_sort):
        min_value = min(list_to_sort)
        sorted_list.append(min_value)
        list_to_sort.remove(min_value)
    return sorted_list

def good_sort(list_to_sort):
    quickSort(list_to_sort,0,len(list_to_sort)-1)


def builtin_sort(list_to_sort):
    list_to_sort.sort()
    return list_to_sort


def partition(arr,low,high):
    i = ( low-1 )         # index of smaller element
    pivot = arr[high]     # pivot

    for j in range(low , high):

        # If current element is smaller than or
        # equal to pivot
        if   arr[j] <= pivot:

            # increment index of smaller element
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def quickSort(arr,low,high):
    if low < high:

        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr,low,high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
