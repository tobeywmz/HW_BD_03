from SocialMedia import SocialMedia

class Twitter(SocialMedia):
    
  def __init__(self, name, body):
      super().__init__(name)
      slef.body = body
      
Tweets= []


def CreateNewTweet(Tweet):
    print('Enter the body of your new tweet:')
    body = input()

    if len(body)<280:
        Tweets.append(body)

def GetTweets():
    return self.Tweets

i=0
while i<1:
    print('Do you want to create a new tweet?(yes/no)')
    answer = input()
      
    if answer == 'yes':
          CreateNewTweet(Tweets)
          
    elif answer == 'no':
          print('your tweets are:')
          print(Tweets)
          i= i+1
