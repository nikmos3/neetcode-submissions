class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mapp = defaultdict(list)

        for a,b in prerequisites:
            mapp[a].append(b)
        
        visiting = set()
        visited = set()
        

        def explore(node):
            if node in visited:
                return False
            
            if node in visiting:
                return True

            visiting.add(node)

            for n in mapp[node]:
                if explore(n):
                    return True
            visiting.remove(node)
            visited.add(node)

            return False

        for i in range(numCourses):
            if explore(i):
                return False
        return True
        