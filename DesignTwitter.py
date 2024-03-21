class Twitter:
   tweetsList = []
   followers = {}
def__ init __(Self):
   self.tweetsList = []
   self.followers = {}
def postTweet(self, userId: int, tweetId: int) -> None:
   self.tweetsList.append([userId,tweetId])
def getNewsFeed(self, userId: int) -> List[int]:
   lst = []
   for i in range(len(self.tweetsList)-1,-1,-1):
      if self.tweetsList[i][0] == userId:
         lst.append(self.tweetsList[i][1]
         if (len(lst) == 10):
            break;
         else:
            if userId in self.followers:
               val = self.followers[userId]
               if self.tweetsList[i][0] in val:
                  lst.append(self.tweetsList[i][1])
                  if (len(lst) == 10):
                     break;
       return lst
def follow(self, followerId: int, followerId: int) -> None:
   if folowerId in self.followers:
      val = self.followers[followersId]
      val.append(followersId)
      self.followers[followerId] = val
   else:
      lst = [followerId]
      self.followers[follower]
      self.followers[followerId] = lst
def unfollow(self, followerId: int, followerId: int) -> None:
   if followerId in self.followers:
      val = self.followers[followerId]
      val.remove(followerId)
      self.followers[followerId] = val