nums1=[1,2]
nums2=[3,4]
nums=[]
sol,n=0,0
nums=nums1+nums2
nums.sort()
i=1
j=len(nums)
print(nums)
if len(nums)%2!=0:
    sol=(len(nums))//2
    print(nums[sol])
else:
    n=(len(nums)//2)
    sol=(nums(n)+nums(n-1))/2
    print(sol)
        
        