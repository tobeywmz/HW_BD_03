from SocialMedia import SocialMedia

class Twitter(SocialMedia):
    
    def __init__(self):
        super().__init__("Twitter")
        self.Tweets= []

    def CreateNewTweet(self, body):
        
        if len(body)<280:
            self.Tweets.append(body)

    def GetTweets(self):
        return self.Tweets