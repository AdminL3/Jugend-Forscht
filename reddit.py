import praw

reddit = praw.Reddit(client_id='TuiogymjZuYU0QKXhorR_A',
                     client_secret='hNv2Jlu5SDFHUF9rd8_75KycDb5Gqg',
                     user_agent='Admin_L3')


subreddit = reddit.subreddit('PrisonBreak')
for post in subreddit.hot(limit=5):
    print(f'Title: {post.title}, Score: {post.score}')
