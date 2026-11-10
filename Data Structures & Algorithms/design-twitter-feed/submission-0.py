class Twitter:

    def __init__(self):
        self.tweets =  defaultdict(list)  # userId -> list of (timestamp, tweetId)
        self.follows = defaultdict(set) # userid -> set of people it follows
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        users = [userId]
        if userId in self.follows:
            users.extend(self.follows[userId])

        # Add the newest tweet of each user to the heap
        for authorId in users:
            if self.tweets[authorId]:
                index = len(self.tweets[authorId]) - 1
                timestamp, tweetId = self.tweets[authorId][index]
                heap.append((-timestamp, tweetId, authorId, index))

        heapq.heapify(heap)

        news_feed = []
        while heap and len(news_feed) < 10:
            negative_timestamp, tweetId, authorId, index = heapq.heappop(heap)
            news_feed.append(tweetId)

            # wenn 1 user nur 3 tweets hat und 1 anderer nur 4tweets usw
            # prev tweet from same author
            previous_index = index - 1 
            if previous_index >= 0:
                timestamp, previous_tweetId = self.tweets[authorId][previous_index]

                heapq.heappush(
                    heap,
                    (-timestamp, previous_tweetId, authorId, previous_index)
                )
        return news_feed


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            self.follows[followerId].discard(followeeId)

            if len(self.follows[followerId]) == 0:
                del self.follows[followerId]
