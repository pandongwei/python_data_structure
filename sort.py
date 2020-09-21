# 冒泡排序， O(n2)
def BubbleSort(nums):
    l = len(nums)
    for i in range(l):
        for j in range(l-1,i,-1):
            if nums[j-1] > nums[j]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
    return nums

# 选择排序， O(n2)
def SelectSort(nums):
    l = len(nums)
    for i in range(l):
        min = i
        for j in range(i+1, l):
            if nums[j] < nums[min]:
                min = j
        if i != min:
            nums[i], nums[min] = nums[min], nums[i]
    return nums

# 插入排序， O(n2)
def InsertSort(nums):
    l = len(nums)
    for i in range(1, l):
        if nums[i] < nums[i-1]:
            tmp = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > tmp:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = tmp
    return nums

# 希尔排序，插入排序的升级版，O(nlogn)
def shellSort(nums):
    l = len(nums)
    if l==1 or l==0: return nums
    increment = l // 2
    while increment >= 1:
        for i in range(increment, l):
            j = i
            while j >= increment and nums[j] < nums[j-increment]:
                nums[j], nums[j-increment] = nums[j-increment], nums[j]
                j -= increment
        increment //= 2
    return nums

# 堆排序 O(nlogn)
# 数组创建一个最大堆；开始迭代，每次堆首与堆尾互换，堆尺寸缩小1，并且再次调整位置形成最大堆
# 重复上述步骤直至结束
def HeapSort(nums):
    l = len(nums)
    def heapify(nums, i):
        left, right, largest = 2*i+1, 2*i+2, i
        if left < l and nums[left] > nums[largest]:
            largest = left
        if right < l and nums[right] > nums[largest]:
            largest = right
        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            heapify(nums, largest)
    def buildMaxHeap(nums):
        for i in range(len(nums)//2, -1, -1):
            heapify(nums, i)
    buildMaxHeap(nums)
    for i in range(len(nums)-1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        l -= 1
        heapify(nums, 0)
    return nums

# 归并排序 递归 O(nlogn)
# 把数组分为多个小数组排序，然后往上合并，每两个有序数组进行合并
def mergeSort_digui(nums):
    def merge(nums_l, nums_r):
        res = []
        while nums_l and nums_r:
            if nums_l[0] <= nums_r[0]:
                res.append(nums_l.pop(0))
            else:
                res.append(nums_r.pop(0))
        while nums_l:
            res.append(nums_l.pop(0))
        while nums_r:
            res.append(nums_r.pop(0))
        return res
    l = len(nums)
    if l < 2: return nums
    mid = l//2
    nums_l, nums_r = nums[:mid], nums[mid:]
    return merge(mergeSort_digui(nums_l), mergeSort_digui(nums_r))

# 归并排序 迭代
def mergeSort_diedai(nums):
    pass

# def QuickSort(nums):
#     def QSort(nums, low, high):
#         if low < high:
#             pivot = Partition(nums, low, high)
#             QSort(nums, low, pivot-1)
#             QSort(nums, pivot+1, high)
#     def Partition(nums, low, high):
#         pivotkey = nums[low]
#         while low < high:
#             while low < high and nums[high] >= pivotkey:
#                 high -= 1
#             nums[low], nums[high] = nums[high], nums[low]
#             while low < high and nums[low] <= pivotkey:
#                 low += 1
#             nums[low], nums[high] = nums[high], nums[low]
#         return low
#     l = len(nums)
#     QSort(nums, 0, l-1)
#     return nums

# 快速排序，O(nlogn)
def quickSort(nums):
    def Qsort(nums, left, right):
        if left >= right: return
        low, high = left, right
        pivot = nums[low]
        while left < right:
            while left < right and pivot <= nums[right]:
                right -= 1
            nums[left] = nums[right]
            while left < right and pivot >= nums[left]:
                left += 1
            nums[right] = nums[left]
        nums[left] = pivot
        Qsort(nums,low,left-1)
        Qsort(nums,left+1,high)
    Qsort(nums,0,len(nums)-1)
    return nums

# 桶排序 O(n+k)
def bucketSort(nums):
    pass

# 计数排序，O(n+k),k为数组的范围
def countingSort(nums):
    l = len(nums)
    min, max = nums[0], nums[0]
    for i in range(1, l):
        if nums[i] < min: min = nums[i]
        if nums[i] > max: max = nums[i]
    bucket = [0 for i in range(max-min+1)]
    for i in range(l):
        bucket[nums[i]-min] += 1
    j = 0
    for i in range(len(bucket)):
        while bucket[i] > 0:
            nums[j] = i+min
            j += 1
            bucket[i] -= 1
    return nums

# 基数排序,O(kn),k为位数通常很小
# 将所有数值统一为同样的数位长度，需要补零
# 从最低位开始，根据该位的数进行排序（需要建立10个桶，从0-9）
# 历遍至最高位，则完成排序
def indexSort(nums):
    pass

test = [10,9,8,7,6,5,4,3,2,1,0]
test1 = [8,8,4,7,1,2,1,3,10,5,0]
HeapSort(test)
print(test)