import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        # creating a list of prerequisites for each course
        prereq = collections.defaultdict(list)
        for c, p in prerequisites:
            prereq[c].append(p)

        # recursive dfs
        def dfs(course):
            # if course has been visited, we know it's a cycle return
            if course in visited:
                return False
            # if no prereqs for that course we can return empty list
            if prereq[course] == []:
                return True

            # add course to visited
            visited.add(course)
            for req in prereq[course]:
                # reursively call dfs and check if a cycle exists right away, if it does then return False
                if not dfs(req):
                    return False
            # remove the course from visited since we are only checking visited cells for the current path we are on
            # if we didn't remove a course from the visited graph, it could trip in the first if statement and return false
            # even though the course doesn't have a cycle
            visited.remove(course)
            # set the prereq list for that course to an empty list
            prereq[course] = []
            return True

        # looping through course numbers
        for course in range(numCourses):
            # if any courses have cycle we can immediately return False
            if not dfs(course):
                return False
        return True

