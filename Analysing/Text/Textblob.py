from textblob import TextBlob

# # Load the file
# file = r"text.txt"
# with open(file, 'r', encoding='utf-8') as f:
#     text = f.read()

text = '''
'''
# Create TextBlob object
blob = TextBlob(text)

# Sentiment analysis
sentiment_polarity = blob.sentiment.polarity
if sentiment_polarity > 0:
    sentiment_type = "Positive 😀"
elif sentiment_polarity < 0:
    sentiment_type = "Negative 😠"
else:
    sentiment_type = "Neutral 😐"

# Subjectivity analysis
sentiment_subjectivity = blob.sentiment.subjectivity
subjectivity_type = "Objective 😀" if sentiment_subjectivity < 0.5 else "Subjective 😠"
sentiment_subjectivity_new = int(
    abs(((sentiment_subjectivity * 100) * 2) - 100))

# Output results
result = f"{sentiment_type} ({int(abs(sentiment_polarity * 100))}%)"
print("The text is very " + result)

result = f"{subjectivity_type} ({sentiment_subjectivity_new}%)"
print("and also " + result)
