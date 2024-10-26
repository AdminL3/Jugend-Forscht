import config
import praw
reddit = praw.Reddit(client_id=config.client_id,
                     client_secret=config.client_secret,
                     user_agent=config.user_agent)
subreddit = reddit.subreddit('PrisonBreak')
for post in subreddit.hot(limit=5):
    print(f'Title: {post.title}, Score: {post.score}')
