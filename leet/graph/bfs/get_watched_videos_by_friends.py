# https://leetcode.com/problems/get-watched-videos-by-your-friends/

from collections import defaultdict, deque
from typing import List

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        
        friends_at_dist = set()

        q = deque([id])
        dist = 1
        visited = set([id])

        while q:
            next_level = set()
            for _ in range(len(q)):
                node = q.popleft()

                for nei in friends[node]:
                    if nei not in visited and nei not in next_level:
                        next_level.add(nei)
                        q.append(nei)
            if dist == level:
                friends_at_dist = next_level
                break
            visited.update(next_level)
            dist += 1
        
        videos = defaultdict(int)
        for friend in friends_at_dist:
            for vid in watchedVideos[friend]:
                videos[vid] += 1
        
        video_list = []
        for vid, f in videos.items():
            video_list.append((f, vid))
        
        video_list.sort(key=lambda x: (x[0], x[1]))

        return [vid for _, vid in video_list]