class BiTNode():
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

T = BiTNode(1)
def SearchBST(T, key, f, p):
    # 查找失败，返回访问的最后一个节点
    if T is None:
        p = f
        return p, False
    # 查找成功，返回当前数据节点
    elif key == T.data:
        p = T
        return p, True
    # 递归查找
    elif key < T.data:
        return SearchBST(T.lchild, key, T, p)
    else:
        return SearchBST(T.rchild, key, T, p)

def InsertBST(T, key):
    p, res = SearchBST(T, key, None, None)
    if res is False:
        s = BiTNode(key)
        if p is None:
            T = s
        elif key < p.data:
            p.lchild = s
        else:
            p.rchild = s
        return True
    else:
        return False

# 这里的T是指一棵树的根节点
def DeleteBST(T, key):
    if T is None:
        return False
    else:
        if key == T.data:
            return Delete(T)
        elif key < T.data:
            return DeleteBST(T.lchild, key)
        else:
            return DeleteBST(T.rchild, key)

def Delete(p):
    if p.rchild == None:
        q = p
        p = p.lchild
    elif p.lchild == None:
        q = p
        p = p.rchild
    else:
        q = p
        s = p.lchild
        while s.rchild != None:
            q = s
            s = s.rchild
        p.data = s.data
        if q != s:
            q.rchild = s.lchild
        else:
            q.lchild = s.lchild
    return True

