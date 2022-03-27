from SocialMedia import SocialMedia

class Instagram(SocialMedia):
    
    def __init__(self):
        super().__init__("Instagram")
        self.Posts= []

    def PublishNewPost(self, body):
        if len(body)<2200:
            self.Posts.append(body)

    def GetPosts(self):
        return self.Posts