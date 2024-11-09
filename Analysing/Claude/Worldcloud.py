import os
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
from datetime import datetime

import json


# Download required NLTK data
nltk.download('stopwords')
nltk.download('punkt')


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


def generate_topic_wordclouds(df, output_dir="data/wordclouds"):
    """
    Generate and save word clouds for each topic
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Get stopwords
    stop_words = set(stopwords.words('english'))
    # Add custom stopwords relevant to news articles
    custom_stops = {'said', 'would', 'could', 'one',
                    'also', 'year', 'years', 'new', 'time'}
    stop_words.update(custom_stops)

    def process_text(text):
        # Tokenize and clean text
        tokens = word_tokenize(text.lower())
        # Remove stopwords, punctuation, and short words
        words = [word for word in tokens
                 if word.isalnum() and
                 word not in stop_words and
                 len(word) > 3]
        return ' '.join(words)

    # Generate word cloud for each topic
    for topic in df['topic'].unique():
        # Get all text for this topic
        topic_text = df[df['topic'] == topic]['content'].str.cat(sep=' ')

        # Process text
        processed_text = process_text(topic_text)

        # Create word cloud
        wordcloud = WordCloud(
            width=1600,
            height=800,
            background_color='white',
            max_words=100,
            colormap='viridis',  # You can change the colormap
            contour_width=3,
            contour_color='steelblue'
        ).generate(processed_text)

        # Create figure with high resolution
        plt.figure(figsize=(20, 10), dpi=300)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title(f'Word Cloud - {topic.capitalize()}', fontsize=24, pad=20)

        # Save the word cloud
        filename = f"{topic}_wordcloud.png"
        plt.savefig(os.path.join(output_dir, filename),
                    bbox_inches='tight',
                    dpi=300)
        plt.close()

        # Also save word frequencies as JSON for reference
        word_freq = Counter(processed_text.split())
        top_words = dict(sorted(word_freq.items(),
                                key=lambda x: x[1],
                                reverse=True)[:100])

        with open(os.path.join(output_dir, f"{topic}_frequencies.json"), 'w') as f:
            json.dump(top_words, f, indent=2)

        print(f"Generated word cloud for {topic}")
        print(f"Top 10 words in {topic}:")
        for word, freq in list(top_words.items())[:10]:
            print(f"  {word}: {freq}")


# Load and process your data
topics = ["politics", "world"]
start_year = 2020
amount_years = 2

# Load articles (using your existing loading code)
articles_df = load_nyt_articles(
    "data/articles", topics, start_year, amount_years)

# Generate word clouds
generate_topic_wordclouds(articles_df)

print("\nWord clouds have been saved to data/wordclouds/")
