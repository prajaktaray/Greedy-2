# Leetcode: Pass
#TC-O(max(time,total_task_len)), SC- O(1)
# 1) create an noOfTask array keeping the count of occurence of chars
# 2) sort the array to push valid chars to the end of array
# 3) while noOfTask has valid chars
# 3.1) keep increasing the count and time while count<= least number of intervals(n)
# 3.2) reset count to start a new stage
# 3.3) keep sorting the array
    pass
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        noOfTask = [0]*26
        #1
        for ch in tasks:#O(n)
            noOfTask[ord(ch)-ord('A')] +=1
        #2
        noOfTask.sort()#O(total_task_len)
        count =0
        time=0
        #3
        while(noOfTask[25]>0):
            #3.1
            while(count<=n and noOfTask[25]>0):
                if(count < 26and noOfTask[25 - count]>0):
                    #decrease the occurenceof the char once considered
                    noOfTask[25 - count] -=1
                count +=1
                time +=1
            #3.2
            count = 0
            #3.3
            noOfTask.sort()
        return time#O(time)
