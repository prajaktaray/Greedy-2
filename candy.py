#Leetcode : Pass
# TC- O(n), SC-O(n)...considering the new candies array created
# 1) initialize candies array of size of ratings with 1 as each child must have atleast 1candy
# 2) iterate from left to satisfy "Children with a higher rating get more candies than their neighbors"
#    and add +1
# 3) similar to 2 iterate from right to check and update to satisfy condition

class Solution:
    def candy(self, ratings: List[int]) -> int:
        #1
        candies = [1]*len(ratings)
        #2
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]: candies[i] = candies[i-1]+1
        #3
        for i in range((len(ratings)-2),-1,-1):
            if ratings[i]>ratings[i+1]: candies[i] =max(candies[i],candies[i+1]+1)
        return sum(candies)
