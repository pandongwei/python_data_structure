# 冒泡排序
def BubbleSort(nums):
    l = len(nums)
    for i in range(l):
        for j in range(l-1,i,-1):
            if nums[j-1] > nums[j]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
    return nums

# 选择排序
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

# 插入排序
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

# 希尔排序
def ShellSort(nums): #TODO
    l = len(nums)
    increment = l
    acc = 0
    while increment >=1 and acc == 0:
        increment = increment // 3 + 1
        if increment == 1:
            acc = 1
        for i in range(increment, l):
            if nums[i] < nums[i-increment]:
                tmp = nums[i]
                j = i - increment
                while j >= 0 and nums[j] > tmp:
                    nums[j+increment] = nums[j]
                    j -= increment
                nums[j+increment] = tmp
    return nums


def shellSort(nums):
    n = len(nums)
    gap = int(n / 2)
    while gap > 0:
        for i in range(gap, n):
            temp = nums[i]
            j = i
            while j >= gap and nums[j - gap] > temp:
                nums[j] = nums[j - gap]
                j -= gap
            nums[j] = temp
        gap = int(gap / 2)
    return nums

# 堆排序
def HeapSort(nums):
    pass

# 归并排序
def merge_sort(a: List[int]):
    _merge_sort_between(a, 0, len(a) - 1)

def _merge_sort_between(a: list[int], low: int, high: int):
    # The indices are inclusive for both low and high.
    if low < high:
        mid = low + (high - low) // 2
        _merge_sort_between(a, low, mid)
        _merge_sort_between(a, mid + 1, high)
        _merge(a, low, mid, high)

def _merge(a: list[int], low: int, mid: int, high: int):
    # a[low:mid], a[mid+1, high] are sorted.
    i, j = low, mid + 1
    tmp = []
    while i <= mid and j <= high:
        if a[i] <= a[j]:
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[j])
            j += 1
    start = i if i <= mid else j
    end = mid if i <= mid else high
    tmp.extend(a[start:end + 1])
    a[low:high + 1] = tmp

def QuickSort(nums):
    def QSort(nums, low, high):
        if low < high:
            pivot = Partition(nums, low, high)
            QSort(nums, low, pivot-1)
            QSort(nums, pivot+1, high)
    def Partition(nums, low, high):
        pivotkey = nums[low]
        while low < high:
            while low < high and nums[high] >= pivotkey:
                high -= 1
            nums[low], nums[high] = nums[high], nums[low]
            while low < high and nums[low] <= pivotkey:
                low += 1
            nums[low], nums[high] = nums[high], nums[low]
        return low
    l = len(nums)
    QSort(nums, 0, l-1)
    return nums

def quick_sort(nums,left,right):
    if left >= right: return
    low, high = left, right
    pivotkey = nums[low]
    while left < right:
        while left < right and nums[right] > pivotkey:
            right -= 1
        nums[left] = nums[right]
        while left < right and nums[left] <= pivotkey:
            left += 1
        nums[right] = nums[left]
    nums[right] = pivotkey
    quick_sort(nums, low, left-1)
    quick_sort(nums, left+1, right)


test = [10,9,8,7,6,5,4,3,2,1,0]
test1 = [8,6,4,7,9,2,1,3,10,5,0]
print(QuickSort(test))