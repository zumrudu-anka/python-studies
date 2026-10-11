import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "#SağlıktaŞiddet"
tweets = []
tweet_limit = 5000

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if len(tweets) == tweet_limit:
        break
    else:
        tweets.append([
            pd.to_datetime(tweet.date).date(),
            tweet.user.username,
            tweet.rawContent,
            tweet.renderedContent
        ])

df = pd.DataFrame(tweets, columns = ["Date", "User", "RawContent", "Rendered Content"])
df.index += 1
df.to_excel("tweets.xlsx", header = True, index = True)