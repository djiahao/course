
# coding: utf-8

# In[1]:

class SingleNode(object):
    """单链表的节点"""
    def __init__(self, item):
        self.item = item
        self.next = None
        
class SingleLinkList(object):
    """单链表"""
    def __init__(self, node = None):
        self.__head = node
        
    def is_empty(self):
        """链表是否为空"""
        return self.__head == None
    
    def length(self):
        """链表长度"""
        cur = self.__head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count
    
    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur != None:
            print(cur.item)
            cur = cur.next
    
    def add(self, item):
        """链表头部添加元素"""
        node = SingleNode(item)
        node.next = self.__head
        self.__head = node
    
    def append(self, item):
        """链表尾部添加元素"""
        node = SingleNode(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
    
    def insert(self, pos, item):
        """指定位置添加元素"""
        pass
    
    def remove(self, item):
        """删除节点"""
        pass
    
    def search(self, item):
        """查找节点是否存在"""
        pass
    
if __name__ == "__main__":
    node1 = SingleLinkList()
    node1.add(13)
    node1.add(8)
    node1.append(4)
    node1.append(45)
    print(node1.is_empty())
    print(node1.length())
    node1.travel()
    
    


# In[ ]:



