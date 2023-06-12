class Solution(object):
  '''
  Exercise 1:
  Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

  Example 1:

  Input: nums = [1,2,3,1]
  Output: true
  Example 2:

  Input: nums = [1,2,3,4]
  Output: false'''

  def containsDuplicate(self, nums):
      return len(nums) != len(set(nums))

  '''
  Exercise 2:
  Given two strings s and t, return true if t is an anagram of s, and false otherwise.

  An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

  Example 1:

  Input: s = "anagram", t = "nagaram"
  Output: true
  Example 2:

  Input: s = "rat", t = "car"
  Output: false
  '''

  def isAnagram(self, s, t):
      return sorted(list(s)) == sorted(list(t))

  '''
  Exercise 3:
  Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

  Specifically, ans is the concatenation of two nums arrays.

  Return the array ans.

  Example 1:

  Input: nums = [1,2,1]
  Output: [1,2,1,1,2,1]
  Explanation: The array ans is formed as follows:
  - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
  - ans = [1,2,1,1,2,1]'''

  def getConcatenation(self, nums):
      return nums*2
