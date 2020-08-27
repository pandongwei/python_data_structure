


def search(nums, target: int) -> int:
    left, right = 0, len(nums)-1
    if right == -1: return 0
    if right == 0:return int(nums[0]==target)
    ans = 0
    while left <= right:
        mid = left + (right - left)//2
        if nums[mid] == target:
            ans += 1
            break
        elif nums[mid] > target:
            right = mid-1
        else:
            left = mid+1
    if ans == 0:
        return 0
    else:
        tmp = mid
        while mid > 0:
            mid -= 1
            if nums[mid] != target:
                break
            ans += 1
        while tmp < len(nums)-1:
            tmp += 1
            if nums[tmp] != target:
                break
            ans += 1
        return ans

print(search([5,7,7,8,8,10], 8))