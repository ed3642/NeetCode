from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.followerMap = defaultdict(set) # userId -> followeeId 
        self.tweets = defaultdict(list) # userId -> tweetId
        self.order = 0 # order of tweets

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.order, tweetId))
        self.order -= 1

    def getNewsFeed(self, userId: int) -> list[int]:
        res = []
        heap = []

        # builds latest tweets heap
        self.followerMap[userId].add(userId) # all users follow themselves
        for followeeId in self.followerMap[userId]:
            if followeeId in self.tweets:
                lastTweetIndex = len(self.tweets[followeeId]) - 1
                order, tweetId = self.tweets[followeeId][lastTweetIndex]
                heapq.heappush(heap, [order, tweetId, followeeId, lastTweetIndex - 1])

        # gets top 10 tweets
        while heap and len(res) < 10:
            order, tweetId, followeeId, lastTweetIndex = heapq.heappop(heap)
            res.append(tweetId)
            if lastTweetIndex >= 0:
                order, tweetId = self.tweets[followeeId][lastTweetIndex]
                heapq.heappush(heap, [order, tweetId, followeeId, lastTweetIndex - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followerMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followerMap:
            self.followerMap[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)