import heapq
class Twitter:

    def __init__(self):
        self.time=0
        self.tweetmap=defaultdict(list) # userId--> list ([time,tweeId])
        self.followmap=defaultdict(set)  # userId--> set of followee
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append([self.time,tweetId])
        self.time+=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        pq=[]
        res=[]
        self.followmap[userId].add(userId)
        for followeeId in self.followmap[userId]:
            ind=len(self.tweetmap[followeeId])-1
            if ind>=0:
                time,tweetid=self.tweetmap[followeeId][ind]
                heapq.heappush(pq,[-time,tweetid,followeeId,ind-1])
        while pq and len(res)<10:
            time,tweetid,followeeId,ind=heapq.heappop(pq)
            res.append(tweetid)
            if ind>=0:
                time,tweetid=self.tweetmap[followeeId][ind]
                heapq.heappush(pq,[-time,tweetid,followeeId,ind-1])
        return res



    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)