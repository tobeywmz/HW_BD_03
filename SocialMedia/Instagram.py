from SocialMedia import SocialMedia

class Instagram(SocialMedia):
    
  def __init__(self, name, body):
      super().__init__(name)
      slef.body = body
      
Posts= []


def PublishNewPost(Post):
    print('Enter the body of your new post:')
    body = input()

    if len(body)<2200:
        Posts.append(body)

def GetPosts():
    return self.Posts
    

w=0
while w<1:
    print('Do you want to make a new post?(yes/no)')
    answer = input()
      
    if answer == 'yes':
          PublishNewPost(Posts)
          
    elif answer == 'no':
          print('your posts are:')
          print(Posts)
          w= w+1

