def binary_search(arr, x):
    """
    使用二分法在数组 arr 中查找 x
    如果找到，返回 x 的索引，否则返回 -1
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        # 检查 x 是否存在于中间位置
        if arr[mid] == x:
            return mid
        # 如果 x 大于中间位置的值，只需查找右边
        elif arr[mid] < x:
            left = mid + 1
        # 否则只需查找左边
        else:
            right = mid - 1
    # 如果我们到达这里，那么元素不在数组中
    return -1

# 示例
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 5
result = binary_search(arr, x)

if result != -1:
    print(f"Element {x} is at index {result}")
else:
    print(f"Element {x} is not present in array")
