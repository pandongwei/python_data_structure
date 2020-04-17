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

def PreTraversal(root):
    if root != None:
        print(root.val)
        PreTraversal(root.left)
        PreTraversal(root.right)