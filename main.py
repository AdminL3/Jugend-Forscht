from textblob import TextBlob


print("Input text:")
text = input()

blob = TextBlob(text)
sentiment_polarity = blob.sentiment.polarity
if sentiment_polarity > 0:
    sentiment_type = "Positive 😀"
elif sentiment_polarity < 0:
    sentiment_type = "Negative 😠"
else:
    sentiment_type = "Neutral 😐"


sentiment_subjectivity = blob.sentiment.subjectivity
sentiment_subjectivity_new = int(abs(((sentiment_subjectivity*100)*2)-100))

if sentiment_subjectivity < 0.5:
    subjectivity_type = "Subjective 😀"
else:
    subjectivity_type = "Objective 😠"

result = f"{sentiment_type} ({int(abs(sentiment_polarity*100))}%)"
print("The text is very " + result)


result = f"{subjectivity_type} ({sentiment_subjectivity_new}%)"
print("and also " + result)
