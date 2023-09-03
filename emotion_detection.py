from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator  # Import the IAMAuthenticator class



# Replace these with your own credentials
API_KEY = "6bbda3b3-d572-45e1-8c54-22d6ed9e52c2"
API_URL = "https://api.eu-gb.natural-language-understanding. watson.cloud.ibm.com/instances/4bce0063-2b11-4e4a-913e-90e68e8e16c6"

authenticator=IAMAuthenticator(API_KEY)

# Create a NaturalLanguageUnderstanding client
nlu_client = NaturalLanguageUnderstandingV1(
    version="2021-08-01",
    authenticator=authenticator,
)
 


# Get user input for the text to analyze
text = input("Enter the sentence to analyze sentiment: ")

# Analyze sentiment
response = nlu_client.analyze(
    text=text,
    features=Features(sentiment=SentimentOptions())
).get_result()

# Extract sentiment score
sentiment_score = response['sentiment']['document']['score']

# Interpret sentiment score
if sentiment_score > 0.5:
    sentiment_label = "positive"
elif sentiment_score < -0.5:
    sentiment_label = "negative"
else:
    sentiment_label = "neutral"

# Print results
print("Text:", text)
print("Sentiment:", sentiment_label)
print("Sentiment Score:", sentiment_score)
