#!/usr/bin/env python3

nums = [16, 15, 12, 5, 19, 6]

p = []
i = 1
while i < len(nums)-1:
    if nums[i-1] < nums[i] > nums[i+1]:
        p.append(nums[i])
    i += 1

print(p)