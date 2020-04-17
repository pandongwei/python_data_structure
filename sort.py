def BubbleSort(nums):
    l = len(nums)
    for i in range(l):
        for j in range(l-1,i-1,-1):
            if nums[j-1] > nums[j]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
    return nums

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

def HeapSort(nums):
    pass

def MSort(nums):
    pass

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

test = [10,9,8,7,6,5,4,3,2,1,0]
test1 = [8,6,4,7,9,2,1,3,10,5,0]
print(QuickSort(test1))