class Solution:
  def findLonely(self, nums: List[int]) -> List[int]:
    nums.sort()
    result = []
    n = 0
    for _ in nums:
      n += 1
    for i in range(n):
      if i > 0 and (nums[i] == nums[i - 1] or nums[i] == nums[i - 1] + 1):
        continue
      if i < n - 1 and (nums[i] == nums[i + 1] or nums[i] == nums[i + 1] - 1):
        continue

      result.append(nums[i])

    return result