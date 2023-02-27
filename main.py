class Solution(object):
  def isPalindrome(self, x):
    self.x = x   
  def myfunc():
    x = -10
    print(x)
    print(str(x)[::-1])
    
    if x<0 or (x > 0 and x%10 == 0):
      print("false")
      return(False)
    elif  x == int(str(x)[::-1]):
      print("true")
      return(True)
    else:
      print("false")
      return(False)
      
  myfunc()

  































# import itertools

# class Solution(object):
#     def twoSum(self, nums, target):
#        self.nums = nums
#        self.target = target   
#     def myfunc():
#       nums = [2,7,11,15]
#       no = nums.sort()
#       no
#       print(nums)
#       target = 9
#       print("target =", target)

#       for index,num in  enumerate(nums):
#         if target-num in nums[index+1:]:
#            return(index, nums.index(target-num))

#            # for nums in itertools.combinations(nums,2):
#            #   if sum(nums) == target:
#            #      #print(list(nums))
#            listx = list(nums)
#            print("numbers that are added: ", listx)
#            #print(nums.index(1))
#            #return[int(nums.index(x), nums.index(y))]
#            #return[nums.index[nums,2]]
  
#     indexno = myfunc()
#     print("indexes of numbers: ", indexno)
















# class Solution(object):
#    def twoSum(self, nums, target):
#       self.nums = nums
#       self.target = target   
#    def myfunc():
#      nums = [3,3]
#      no = nums.sort()
#      no
#      print(nums)
#      target = 6
#      print("target =", target)
#      for x in nums:
#        for y in nums [nums.index(x):]:
#         if x+y==target:
#           listx = [x,y]
#           print("numbers that are added: ", listx)
#           #return[int(nums.index(x), nums.index(y))]
#           return[nums.index(int(x)), nums.index(int(y))]
  
#    indexno = myfunc()
#    print("indexes of numbers: ", indexno)
      