# 单链表
class SingleNode(object):
    def __init__(self,item):
        self.item = item
        self.next = None

class SingleLinkList(object):
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head == None

    def length(self):
        cur = self._head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self._head
        while cur != None:
            print(cur.item)
            cur = cur.next

    def add(self,item):
        node = SingleNode(item)
        node.next = self._head
        self._head = node

    def append(self,item):
        node = SingleNode(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            else:
                cur.next = node

    def insert(self,pos,item):
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()):
            self.append(item)
        else:
            node = SingleNode(item)
            count = 0
            cur = self._head
            while count < pos -1:
                cur = cur.next
                count += 1
            node.next = cur.next
            cur.next = node

    def remove(self,item):
        cur = self._head
        pre = None
        while cur != None:
            if cur.item == item:
                if not pre:
                    self._head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self,item):
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

# 单向循环链表
class Node(object):
    def __init__(self,item):
        self.item = item
        self.next = None

class SinCycLinkedlist(object):
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head == None

    def length(self):
        if self.is_empty():
            return 0
        count = 1
        cur = self._head
        while cur.next != self._head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        if self.is_empty(): return
        cur = self._head
        print(cur.item)
        while cur.next != self._head:
            cur = cur.next
            print(cur.item)

    def add(self,item):
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = self._head
        else:
            node.next = self._head
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            cur.next = node
            self._head = node

    def append(self,item):
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = self._head
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            cur.next = node
            node.next = self._head

    def insert(self,pos,item):
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            node = Node(item)
            cur = self._head
            count = 0
            while count < pos - 1:
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self,item):
        pass

    def search(self,item):
        if self.is_empty():
            return False
        cur = self._head
        if cur.item == item:return True
        while cur != self._head:
            cur = cur.next
            if cur.item == item:return True
        return False

# 双向循环链表
class Node(object):
    def __init__(self,item):
        self.item = item
        self.next = None
        self.prev = None

class DLinkList(object):
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head == None

    def length(self):
        pass

def nextPermutation(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    l = len(nums)
    a = 0
    for i in range(l - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            for j in range(l - 1, i, -1):
                if nums[i] < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                    break
            nums[i+1:] = nums[i+1:][::-1]
            a = 1
            break
    if a == 0:
        nums = nums[::-1]
    return nums

if __name__ == '__main__':
    nums = [3,2,1]
    print(nextPermutation(nums))