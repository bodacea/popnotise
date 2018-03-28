import twitter


fsecret = open('../../twittersecrets.txt', 'r')
secrets = fsecret.readline()
ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET = secrets.strip().split(',')
ACCESS_TOKEN = ACCESS_TOKEN.strip()
ACCESS_TOKEN_SECRET = ACCESS_TOKEN_SECRET.strip()
CONSUMER_KEY = CONSUMER_KEY.strip()
CONSUMER_SECRET = CONSUMER_SECRET.strip()

auth = twitter.oauth.OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
ta = twitter.Twitter(auth=auth)

fematweets = ta.statuses.user_timeline(screen_name="fema")
femafriends = ta.friends.ids(screen_name="fema")