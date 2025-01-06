class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result=[0]*len(boxes)
        for i in range(len(boxes)):
            if boxes[i]=='1':
                for j in range(len(boxes)):
                    result[j]+=abs(j-i)
        return result