import config

reddit = config.reddit
subreddit = reddit.subreddit('PrisonBreak')
for post in subreddit.hot(limit=5):
    print(f'Title: {post.title}, Score: {post.score}')
