from typing import List
import collections

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # create a set to store the visited nodes
        visited = set()
        # create a set to store the nodes that are in the cycle
        cycle = set()

        # create a dictionary to store the prerequisites
        prereqs = collections.defaultdict(list)
        for c, p in prerequisites:
            prereqs[c].append(p)
        
        output = []

        # create a depth first search function to traverse the graph
        def dfs(course):
            # if the course is in the cycle, then return False
            if course in cycle:
                return False
            
            # if the course is in the visited set, then we know that we have already visited this node and explored all its prereqs so we can return true 
            if course in visited:
                return True 
            
            # add the course to the cycle set
            cycle.add(course)
            # for each prereq of the course, we will recursively call the dfs function on the prereq
            for p in prereqs[course]: 
                if not dfs(p): 
                    return False 
            
            # remove the course from the cycle set since it's no longer in the path we are cheecking 
            cycle.remove(course)
            visited.add(course)
            output.append(course)
            return True 
        
        # run dfs on each course number 
        for c in range(numCourses): 
            if not dfs(c):
                return []
        
        return output
            