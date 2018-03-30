## Twitter scraper notes

### Get raw hashtag data from Twitter

So you'll need a bunch of keys from twitter for this. Here's how to get those: 

* Read the instructions at the top of https://github.com/bodacea/datascienceforbeginners/blob/master/Notebooks/3.2%20Social%20Media%20APIs.ipynb that'll get you the Twitter keys you need

Now let's play... code doesn't quite work yet, but gives you a start

Code notes: 
* Using the Twitter API.  This returns data in json format; we convert this to a pandas dataframe, to make manipulating it easier.  Perhaps I should have stayed with json?
* Doing minimal amount of processing on the returned data, so we have all of it in case one of the fields becomes important later
* Twitter data is paged: you'll only get 15 tweets back from it when you ask for everything on a hashtag. Like a good wanderer, Twitter leaves you a signpost in each page, pointing to the next thing you need to look at.  
* Twitter data is also rate-limited: you can only make so many calls to the API every 15 minutes.  We use time.sleep() to help with that.  Twitter rate limits are listed in https://developer.twitter.com/en/docs/basics/rate-limits.html - for tweets, they're 180 requests every 15 minutes. 

### References etc

Twitter library: need to read these: 
* https://pypi.python.org/pypi/twitter
* https://developer.twitter.com/en/docs/basics/cursoring

### Other things

fematweets = ta.statuses.user_timeline(screen_name="fema")
femafriends = ta.friends.ids(screen_name="fema")


