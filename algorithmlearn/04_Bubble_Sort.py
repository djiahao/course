
# coding: utf-8

# In[4]:

def bubble_sort(alist):
    """冒泡排序"""
    n = len(alist)
    for j in range(n-1,0,-1):
        count = 0
        for i in range(j):
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]
                count += 1
        if 0 == count:
            return

if __name__ == "__main__":
    ll = [59,63,79,99,11,2,87,104,57]
    print("--------------冒泡排序--------------")
    print(ll)
    bubble_sort(ll)
    print(ll)


# In[ ]:



