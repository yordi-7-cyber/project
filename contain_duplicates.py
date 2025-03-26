Class solution():
    def contain_duplicate(self,nums:List[int]) -> bool:
        n-len(nums)
        for i in range (n-1):
            for j in range(i+1,n):
                if nums[i]==nums[j]:
                    return True
            return False
sol=solution()
number=input("Enter Your number:")
nums=list(map(int,number.split()))
result=sol.contain_duplicate(nums)
print(result)
 
