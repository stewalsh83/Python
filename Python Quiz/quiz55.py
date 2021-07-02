#!/usr/bin/env python3

nums = [1, 5, 18, 19, 20, 9]

p = []
i = 1
while i < len(nums)-1:
    if nums[i-1] < nums[i] > nums[i+1]:
        p.append(nums[i])
    i += 1

print(p)