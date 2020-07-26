# 实现二叉树的各种操作
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 由前序和中序遍历恢复树
def reConstructBinaryTreePreTin(pre, tin):
    if len(pre) == 0:
        return None
    root = TreeNode(pre[0])
    TinIndex = tin.index(pre[0])
    root.left = reConstructBinaryTreePreTin(pre[1:TinIndex+1], tin[0:TinIndex])
    root.right = reConstructBinaryTreePreTin(pre[TinIndex+1:], tin[TinIndex+1:])
    return root

# 后序遍历
def PostTraversal(root):
    if root != None:
        PostTraversal(root.left)
        PostTraversal(root.right)
        print(root.val)

# 由中序和后序恢复树
def reConstructBinaryTreeTinPos(tin, pos):
    if len(tin) == 0:
        return None
    root = TreeNode(pos[-1])
    TinIndex = tin.index(pos[-1])
    root.left = reConstructBinaryTreeTinPos(tin[0:TinIndex], pos[0:TinIndex])
    root.right = reConstructBinaryTreeTinPos(tin[TinIndex+1:], pos[TinIndex:-1])
    return root

# 前序遍历
def PreTraversal(root):
    if root != None:
        print(root.val)
        PreTraversal(root.left)
        PreTraversal(root.right)


class Node(object):
    def __init__(self, elem=-1,lchild=None,rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

class Tree(object):
    def __init__(self):
        self.root = Node()
        self.myQueue = []

    def add(self,elem):
        node = Node(elem)
        if self.root.elem == -1:
            self.root = node
            self.myQueue.append(self.root)
        else:
            treeNode = self.myQueue[0]
            if treeNode.lchild == None:
                treeNode.lchild = node
                self.myQueue.append(treeNode.lchild)
            else:
                treeNode.rchild = node
                self.myQueue.append(treeNode.rchild)
                self.myQueue.pop(0)

    # 利用递归来实现遍历
    def front_digui(self,root):
        if root == None:
            return
        print(root.elem),
        self.front_digui(root.lchild)
        self.front_digui(root.rchild)

    def middle_dugui(self,root):
        if root == None:
            return
        self.middle_dugui(root.lchild)
        print(root.elem)
        self.middle_dugui(root.rchild)

    def later_digui(self,root):
        if root == None:
            return
        self.middle_dugui(root.lchild)
        self.middle_dugui(root.rchild)
        print(root.elem)

    # 利用堆栈来实现遍历
    def front_stack(self,root):
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:
                print(node.elem)
                myStack.append(node)
                node = node.lchild
            node = myStack.pop()
            node = node.rchild

    def middle_stack(self,root):
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:
                myStack.append(node)
                node = node.lchild
            node = myStack.pop()
            print(node.elem)
            node = node.rchild

    def postorderTraversal(self,root):
        if root == None:
            return root
        node = root
        stack_1 = []
        stack_2 = []
        stack_1.append(node)
        while stack_1:
            node = stack_1.pop()
            stack_2.append(node)
            if node.lchild:
                stack_1.append(node.lchild)
            if node.rchild:
                stack_2.append(node.rchild)
        while stack_2:
            temp = stack_2.pop()
            print(temp.elem)

    # 层序遍历
    def levelTraversal(self, root):
        if root == None:
            return root
        queue = []
        node =root
        queue.append(node)
        while queue:
            l = len(queue)
            for i in range(l):
                node = queue.pop(0)
                if node.lchild:
                    queue.append(node.lchild)
                if node.rchild:
                    queue.append(node.rchild)
                print(node.elem)

# 测试各种遍历是否正确
def test():
    a = Tree()
    a.add(1)
    a.add(2)
    a.add(3)
    a.add(4)
    a.add(5)
    a.levelTraversal(a.root)

if __name__ == '__main__':
    test()