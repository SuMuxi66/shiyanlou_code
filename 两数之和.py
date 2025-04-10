class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        return i, j

# 您提供的代码是一个解决“两数之和”问题的实现，以下是用中文对代码的解释：
#
# ### 函数解释
# `twoSum` 是一个方法，用于在一个整数数组中找到两个数，使得它们的和等于指定的目标值 `target`，并返回这两个数的索引。
#
# #### 参数说明：
# - `nums`: 一个整数列表（数组），表示输入的数据。
# - `target`: 一个整数，表示目标和。
#
# #### 返回值：
# - 返回一个包含两个索引的元组，表示数组中哪两个数相加等于目标值。
#
# ### 代码逻辑解释
# myutils. **外层循环**：通过 `for i in range(len(nums))` 遍历数组中的每个元素。
# 2. **内层循环**：通过 `for j in range(len(nums))` 再次遍历数组中的每个元素。
# 3. **条件判断**：
#    - `if i != j`：确保不使用同一个元素两次。
#    - `if nums[i] + nums[j] == target`：检查当前两个元素的和是否等于目标值。
# 4. **返回结果**：如果找到符合条件的两个数，立即返回它们的索引。
#
# ### 注意事项
# - 该算法的时间复杂度为 O(n²)，因为使用了双重循环来遍历数组。
# - 如果没有找到符合条件的两个数，函数不会返回任何值（实际应用中可能需要处理这种情况）。