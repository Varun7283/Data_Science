import numpy as np
nums=np.arange(16,dtype='int').reshape(-1,4)
print("orginal array:")
print(nums)
print("new array after swaping first and last row")
nums=nums[[-1,1,2,0]]
print(nums)