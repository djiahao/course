
# coding: utf-8

# In[4]:


def shell_sort(alist):
    """希尔排序"""
    n = len(alist)
    # 计算初始步长
    gap = n // 2
    # print(type(gap))
    while gap > 0:
        # 按步长进行插入排序
        for i in range(gap,n):
            # print(i)
            j = i
            while j>= gap and alist[j-gap] > alist[j]:
                alist[j],alist[j-gap] = alist[j-gap],alist[j]
                j -= gap
        # 得到新的步长
        gap = gap // 2
        
if __name__ == "__main__":
    alist = [32,43,65,3,5,45,7,4,86,34,95,66]
    print("--------------希尔排序--------------")
    print(alist)
    shell_sort(alist)
    print(alist)


# In[ ]:



