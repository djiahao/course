
# coding: utf-8

# In[1]:

class Node(object):
    """双向链表节点"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None
        self.prev = None

class DLinkList(object):
    """双向链表"""
    def __init__(self):
        self.__head = None
        
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
        """遍历链表"""
        cur = self.__head
        while cur != None:
            print(cur.elem)
            cur = cur.next
    
    def add(self, item):
        """链表头部添加"""
        node = Node(item)
        if self.is_empty():
            # 如果是空链表，将__head指向node
            self.__head = node
        else:
            # 将node的next指向__head的头结点
            node.next = self.__head
            # 将__head的头结点的prev指向node
            self.__head = node
            # 将node后继结点的prev指向node
            node.next.prev = node
    
    def append(self, item):
        """链表尾部添加"""
        node = Node(item)
        if self.is_empty():
            # 如果是空链表，将__head指向node
            self.__head = node
        else:
            # 移动到链表尾部
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            # 将尾节点cur的next指向node
            cur.next = node
            # 将node的prev指向cur
            node.prev = cur
                
    def insert(self, pos, item):
        """指定位置添加"""
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            node = Node(item)
            cur = self.__head
            count = 0
            # 移动到指定位置的前一个位置
            while count < (pos - 1):
                count += 1
                cur = cur.next
            # 将node的prev指向cur
            node.prev = cur
            # 将node的next指向cur的下一个结点
            node.next = cur.next
            # 将cur下一个结点的prev指向node
            cur.next.prev = node
            # 将cur的next指向node
            cur.next = node
    
    def remove(self, item):
        """删除节点"""
        if self.is_empty():
            print("此链表为空，无法删除")
        else:
            cur = self.__head
            if cur.elem == item:
                # 如果首节点的元素即是要删除的元素
                if cur.next == None:
                    # 如果链表只有这一个结点
                    self.__head = None
                else:
                    # 将第二个结点的prev设置为None
                    cur.next.prev = None
                    # 将__head指向第二个结点
                    self.__head = cur.next
                return
            while cur != None:
                # 删除中间位置的结点
                if cur.elem == item:
                    if cur.next != None:
                        # 将cur的前一个结点的next指向cur后一个结点
                        cur.prev.next = cur.next
                        # 将cur后一个结点的prev指向cur前一个结点
                        cur.next.prev = cur.prev
                    else:
                        #  此时cur处于尾节点，删除尾节点
                        # 将cur前一个结点的next指向none
                        cur.prev.next = None
                        # 将cur的prev指向none
                        cur.prev = None
                    break
                cur = cur.next

            
    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                print(cur.elem)
            cur = cur.next
        return False
    
if __name__ == "__main__":
    ll = DLinkList()
    ll.add(12)
    ll.add(34)
    ll.append(78)
    ll.insert(3, 8)
    ll.remove(12)
    print(ll.is_empty())
    print(ll.length())
    ll.search(12)
    ll.travel()
    
    


# In[ ]:



