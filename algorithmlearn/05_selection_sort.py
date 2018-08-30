
# coding: utf-8

# In[3]:


def sele_min_sort(alist):
    """选择最小排序"""
    n = len(alist)
    # 需要进行n-1次选择操作
    for j in range(n-1):
        # 记录最小位置
        min_index = j
        # 从j+1位置到末尾选出最小数据
        for i in range(j+1,n):
            if alist[i] < alist[min_index]:
                min_index = i
        # 如果选择出的数据不在正确位置，进行交换
        if min_index != j:
            alist[j],alist[min_index] = alist[min_index],alist[j]

def sele_max_sort(alist):
    """选择最大排序"""
    n = len(alist)
    # 需要进行n-1次选择操作
    for j in range(n-1,0,-1):
        # 记录最大位置
        max_index = j
        # 从j-1位置到末尾选出最大数据
        for i in range(j-1,-1,-1):
            if alist[i] > alist[max_index]:
                max_index = i
        # 如果选择出的数据不在正确位置，进行交换
        if max_index != j:
            alist[j],alist[max_index] = alist[max_index],alist[j]

if __name__ == "__main__":
    alist1 = [54,226,93,17,77,31,44,55,20]
    alist2 = [54,226,93,17,77,31,44,55,20]
    print("--------------选择排序--------------")
    print(alist1)
    sele_min_sort(alist1)
    sele_max_sort(alist2)
    print(alist1)
    print(alist2)


# In[ ]:



