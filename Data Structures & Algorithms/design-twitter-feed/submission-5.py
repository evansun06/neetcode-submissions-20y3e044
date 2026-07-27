import heapq

class Twitter:

    def __init__(self):
        self.users = {} # user_id : user()
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId] = User(userId)
        
        user = self.users[userId]

        self.time += 1

        user.posts.append((self.time, tweetId))


    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users:
            return []
        
        user = self.users[userId]

        feed = []

        for i in user.following:
            follower = self.users[i]
            for post in follower.posts:
                if len(feed) >= 10:
                    heapq.heappushpop(feed, post)
                else:
                    heapq.heappush(feed, post)

        feed.sort(reverse=True)
            
        return [post[1] for post in feed]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.users:
            self.users[followeeId] = User(followeeId)

        if followerId not in self.users:
            self.users[followerId] = User(followerId)
        
        self.users[followerId].following.add(followeeId)




    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return

        if followerId not in self.users:
            return

        
        if followeeId in self.users[followerId].following:
            self.users[followerId].following.remove(followeeId) 



class User:

    def __init__(self, userId: int):
        self.following = set()
        self.following.add(userId)
        self.posts = []
        

        
