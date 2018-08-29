
# coding: utf-8

# In[9]:

'''
堆排序：
    1.从无序序列建立最大堆（升序构造最大堆）或者最小堆（降序构造最小堆）
    2.利用构建的堆进行排序，取无序序列中第一个元素与最后一个元素交换，最后一个元素即为最终排序好的的有序序列
'''
    
def max_heap_sort(heap):
    '''最大堆排序，适用于升序序列'''
    # 把无序二叉树转换成最大堆
    build_max_heap(heap)
    for i in range(len(heap)-1, -1, -1):
        heap[i],heap[0] = heap[0],heap[i]
        max_heapify(heap, i, 0)
    return heap
    
def min_heap_sort(heap):
    '''最小堆排序，适用于降序序列'''
    # 把无序二叉树转换成最小堆
    build_min_heap(heap)
    for i in range(len(heap)-1, -1, -1):
        heap[i], heap[0] = heap[0],heap[i]
        min_heapify(heap, i, 0)
    return heap
    
def build_max_heap(heap):
    '''
    建立最大堆函数，循环每个根节点，调整堆
    '''
    heap_size = len(heap)
    cur_parents = heap_size // 2 - 1 
    
    # 控制非叶子节点进入比较循环
    for i in range(cur_parents, -1, -1):
        max_heapify(heap, heap_size, i)
        
def max_heapify(heap, heap_size, root):
    '''
    最大堆化: 使父节点比子节点都大
    '''
    
    lchild = root * 2 + 1
    rchild = lchild + 1
    larger = root
    if lchild < heap_size and heap[lchild] > heap[larger]:
        larger = lchild
    if rchild < heap_size and heap[rchild] > heap[larger]:
        larger = rchild
    if larger != root:
        heap[root],heap[larger] = heap[larger],heap[root]
        # 以larger为根节点，重新调整堆
        max_heapify(heap, heap_size, larger)
    
def build_min_heap(heap):
    '''
    建立最小堆函数，循环每个根节点，调整堆
    '''
    heap_size = len(heap)
    cur_parents = heap_size //2 - 1
    
    # 控制非叶子节点进入比较循环
    for i in range(cur_parents, -1, -1):
        min_heapify(heap, heap_size, i)
        
        
def min_heapify(heap, heap_size, root):
    '''
    最小堆化：是父节点比子节点都小
    '''
    
    lchild = root * 2 + 1
    rchild = lchild + 1
    littler = root
    if lchild < heap_size and heap[lchild] < heap[littler]:
        littler = lchild
    if rchild < heap_size and heap[rchild] < heap[littler]:
        littler = rchild
    if littler != root:
        heap[root],heap[littler] = heap[littler],heap[root]
        # 以littler为根节点，重新调整堆
        min_heapify(heap, heap_size, littler)
        
        
        
        
if __name__ == "__main__":
    li = [49,38,65,97,76,13,27,70]
    print(li)
    max_heap_sort(li)
    print(li)
    li2 = [32,42,52,3,45,62,2,63,77]
    print(li2)
    min_heap_sort(li2)
    print(li2)
    
    


# In[ ]:



