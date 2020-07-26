class Node(object):
    def __init__(self, x):
        self.id = x
        self.child = []

def buildTree(nums):
    nums.sort(key=lambda x:x[1])
    head = Node(nums.pop(0)[0])
    node = head
    queue = []
    while nums:
        a, b = nums.pop(0)
        node_new = Node(a)
        queue.append(node_new)
        if b != node.id:
            node = queue.pop(0)
        node.child.append(node_new)
    print(111)

nums = [(1,0),(2,1),(5,2),(6,2),(3,1),(4,1)]
buildTree(nums)