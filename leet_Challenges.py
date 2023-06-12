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

  '''
  Exercise 4:
  Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation: 
- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are no elements to the right of index 5, so we put -1.
  '''

  def replaceElements(self, arr):
      max_so_far = -1
      for i in range(len(arr)-1, -1, -1):
          temp = arr[i]
          arr[i] = max_so_far
          max_so_far = max(max_so_far, temp)
      return arr
  
  '''
  Exercise 5:
  Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false'''

def isSubsequence(self, s, t):
      for char in s:
          found = t.find(char)
          if found == -1:
              return False
          t = t[found+1:]
      return True