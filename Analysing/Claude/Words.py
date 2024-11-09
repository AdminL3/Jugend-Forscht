import os
import pandas as pd
from datetime import datetime
from nltk.sentiment import SentimentIntensityAnalyzer
import re
from collections import Counter


def load_nyt_articles(base_path, topics, start_year, amount_years):
    """
    Load NYT articles matching your exact file structure
    """
    all_articles = []

    for topic in topics:
        print(f"Processing topic: {topic}")
        for i in range(amount_years):
            year = start_year + i
            print(f"Processing year: {year}")

            for j in range(12):
                month = str(j + 1).zfill(2)
                files_path = f"{base_path}/{topic}/{year}/month{month}/"

                if not os.path.exists(files_path):
                    continue

                for file in os.listdir(files_path):
                    if file.endswith('.txt'):
                        file_path = os.path.join(files_path, file)
                        try:
                            with open(file_path, 'r', encoding='utf-8') as f:
                                content = f.read().strip()

                            # Extract date from filename if it exists
                            date_match = re.search(r'(\d{8})', file)
                            if date_match:
                                date_str = date_match.group(1)
                                date = datetime.strptime(date_str, '%Y%m%d')
                            else:
                                # If no date in filename, use year/month
                                date = datetime(year, int(month), 1)

                            # Try to extract title from first line
                            lines = content.split('\n')
                            title = lines[0].strip() if lines else ''
                            article_content = '\n'.join(
                                lines[1:]).strip() if len(lines) > 1 else content

                            article_data = {
                                'date': date,
                                'topic': topic,
                                'title': title,
                                'content': article_content,
                                'year': year,
                                'month': int(month),
                                'filename': file,
                                'word_count': len(article_content.split())
                            }

                            all_articles.append(article_data)

                        except Exception as e:
                            print(f"Error processing {file_path}: {str(e)}")
                            continue

    df = pd.DataFrame(all_articles)
    df = df.sort_values('date')

    print(f"\nLoaded {len(df)} articles:")
    print(f"Date range: {df['date'].min()} to {df['date'].max()}")
    print(f"Articles per topic: {df['topic'].value_counts().to_dict()}")

    return df

# Now let's analyze the data


def analyze_articles_by_topic(df):
    """
    Analyze articles with focus on topic comparison
    """
    # 1. Volume Analysis
    topic_by_month = df.groupby(['topic', 'year', 'month']).size().unstack(0)

    # 2. Content Length Analysis
    length_stats = df.groupby('topic')['word_count'].agg(
        ['mean', 'median', 'count'])

    # 3. Sentiment Analysis
    sia = SentimentIntensityAnalyzer()
    # Sample articles for sentiment analysis to speed up processing
    sample_size = min(1000, len(df))
    sampled_df = df.sample(n=sample_size, random_state=42)
    sampled_df['sentiment'] = sampled_df['content'].apply(
        lambda x: sia.polarity_scores(str(x))['compound']
    )
    sentiment_by_topic = sampled_df.groupby('topic')['sentiment'].mean()

    # 4. Top Terms by Topic
    def get_top_terms(text_series, n=10):
        text = ' '.join(text_series).lower()
        words = text.split()
        words = [w for w in words if len(w) > 3 and w.isalpha()]
        return Counter(words).most_common(n)

    top_terms = {topic: get_top_terms(group['content'])
                 for topic, group in df.groupby('topic')}

    return {
        'volume': topic_by_month,
        'length_stats': length_stats,
        'sentiment': sentiment_by_topic,
        'top_terms': top_terms
    }


# Let's run it with your data
topics = ["politics", "world"]
start_year = 2020  # Adjust this to your start year
amount_years = 2   # Adjust this to your number of years

# Load the data
articles_df = load_nyt_articles(
    "data/articles", topics, start_year, amount_years)

# Run analysis
results = analyze_articles_by_topic(articles_df)

# Print results
print("\n=== Analysis Results ===")
print("\nArticle Counts by Topic and Length:")
print(results['length_stats'])

print("\nAverage Sentiment by Topic:")
print(results['sentiment'])

print("\nTop Terms by Topic:")
for topic, terms in results['top_terms'].items():
    print(f"\n{topic.upper()} top terms:")
    for term, count in terms:
        print(f"  {term}: {count}")
