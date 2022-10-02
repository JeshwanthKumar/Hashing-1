#Time_Complexity: O(n)
#Space_Complexity: 

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0:1} #Initialize a hashmap with the first value as {0:1}
        rSum = 0    #Initialize rSum to 0
        count = 0   #Initialize count to 0
        
        for i in range(len(nums)):  #Loop over the array till the length of nums
            rSum += nums[i] #Calculate rSum to the elements in nums
            compliment = rSum - k   #Calculate compliment which is difference between rSum and k(The sum)
            
            if compliment in hashmap:   #If the compliment value is already in hashmap the increment the count with that value in the hashmap
                count += hashmap[compliment]
            if rSum in hashmap: #If the rSum is already in hashmap then add the rSum with 1
                hashmap[rSum] += 1
            else:   #Else add 1 to rSum in hashmap
                hashmap[rSum] = 1
                
        return count    #Return the count 