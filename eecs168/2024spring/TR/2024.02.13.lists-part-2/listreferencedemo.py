nums1 = [5, 10, 15, 20]
nums2 = nums1

print(nums1)
print(nums2)

nums2[0] = 99
print(nums2)
print(nums1)

nums1[3] = 88
print(nums1)
print(nums2)

nums2 = [100, 200, 300, 400]
print(nums1)
print(nums2)

print('==========')

#Goal: change all the values in nums2
#       to be zero
for item in nums2:
    print(item)
    item = 0
    print(item)

print(nums2)
