
# coding: utf-8

# In[2]:


def insert_sort(alist):
    """插入排序"""
    n = len(alist)
    # 从下标为1的元素开始向前插入
    for i in range(1,n):
        # 从第i个元素开始比较，如果小于前一个元素，进行交换
        for j in range(i,0,-1):
            if alist[j] < alist[j-1]:
                alist[j],alist[j-1] = alist[j-1],alist[j]

if __name__ == "__main__":
    alist = [12,31,55,16,64,88,97,25,75]
    print("--------------插入排序--------------")
    print(alist)
    insert_sort(alist)
    print(alist)




# In[ ]:




# In[ ]:



