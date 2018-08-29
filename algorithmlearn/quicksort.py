def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        low = [i for i in arr[1:] if i <= pivot]
        high = [j for j in arr[1:] if j > pivot]
        return quicksort(low) + [pivot] + quicksort(high)

if __name__ == "__main__":
    li = [2,54,7,45,84,43,25,14,63,92]
    print(li)
    li_sorted = quicksort(li)
    print(li_sorted)
