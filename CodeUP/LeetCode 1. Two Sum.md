# LeetCode/ 1. Two Sum

Given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*.

You may assume that each input would have ***exactly\* one solution**, and you may not use the *same* element twice.

You can return the answer in any order.

medium에서 시작하려다가 영어 해석부터 막혀서 애 먹으면서 시작했습니다. 그래서 가벼운 단어와 설명으로 시작하는 easy 난이도부터 시작해보기로 했습니다. 

위 내용은 

> 정수들의 배열이 nums로 주어지고, 한 개의 정수 값이 target으로 주어질 때,
>
> 두 개의 숫자들의 위치들을 반환해라. 그 두 개의 숫자의 합은 target이다. 

정도로 해석할 수 있는 것 같습니다. 

입력값과 결과값의 예시들은 아래와 같습니다. 

**Example 1:**

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
```

**Example 2:**

```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```



처음에는 아래와 같이 주어져 있는데 

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
```

`def twoSum(self, nums: List[int], target: int) -> List[int]:` 이 표현 자체가 익숙하지 않아서 헷갈렸습니다. 그래서 원래하던 대로 먼저 어떻게 할지 생각하고 적은 다음에 입력해봤는데 "Accepted" !! 

제출

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                trial = nums[i] + nums[j]
                if trial == target:
                    return [i, j]
```

