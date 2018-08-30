
# coding: utf-8

# In[1]:


def merge_sort(alist):
    """归并排序"""
    n = len(alist)
    if n <= 1:
        return alist # 返回拆分子列表
    # 二分分解
    mid_value = n // 2

    left = merge_sort(alist[:mid_value]) 
    right = merge_sort(alist[mid_value:])
    
    return merge(left,right)

def merge(left, right):
    """控制子列表归并算法"""
    # left[],right[]的下标指针
    l, r = 0, 0
    result = [] # 创建存放有序元素的列表
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    # 退出循环，l,r 无论谁先取完子列表所有元素，都追加另一子列表所有元素
    result += left[l:]
    result += right[r:]

    return result

if __name__ == "__main__":
    li = [54,34,53,2,4,45,64,35,77,84,95,35,61]
    print("--------------归并排序--------------")
    sorted_alist = merge_sort(li)
    print(li)
    print(sorted_alist)
    





# In[ ]:



