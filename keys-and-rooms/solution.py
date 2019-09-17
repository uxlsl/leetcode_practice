class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """

        visited = set()

        def f(rooms,to, visited):
            for i in to:
                if i not in visited:
                    visited.add(i)
                    f(rooms, rooms[i], visited)
        f(rooms, [0], visited)
        return len(visited) == len(rooms)
