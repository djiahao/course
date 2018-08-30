
def binarysearch(arr, item):
	"""二分查找"""
	low, high = 0, len(arr)-1
	while low <= high:
		mid = (low + high) // 2
		if item == arr[mid]:
			return print("%s在数组中的索引为%s" % (item, mid))
		elif item < arr[mid]:
			high = mid - 1
		else:
			low = mid + 1
	return print("%s不在该数组中" % item)

if __name__ == '__main__':
	li = [25, 34, 57, 59, 63, 79, 87, 99, 104]
	print("有序数组中的二分查找")
	item = int(input("请输入您要查找的整数："))
	binarysearch(li, item)