import heapq 
from heapq import heappush, heappop, heapify

class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = {}
        for c in s: 
            if c not in counts:
                counts[c] = 1 
            else:
                counts[c] +=1
        
        maxHeap = []
        for c, count in counts.items(): 
            maxHeap.append([-count, c])
        
        heapify(maxHeap) # O(n)
        
        prev = None 
        result = ""

        while maxHeap or prev: 
            if prev and not maxHeap: 
                return ""

            count, char = heappop(maxHeap)
            result += char
            count += 1 

            if prev:
                heappush(maxHeap, prev)
                prev = None 

            if count != 0:
                prev = [count, char]
        
        return result