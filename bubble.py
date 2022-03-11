def bubbleSort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range():
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

nums=eval(input("Enter your List of Number : "))
nums.sort()

print(nums)        