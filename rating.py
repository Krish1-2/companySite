import spacy
import random
from string import punctuation
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nlp = spacy.load('en_core_web_sm')
stop_words = spacy.lang.en.stop_words.STOP_WORDS

def rate(response):
    # Process user responses
    processed_text = ""
   
    new_text = nlp(response)
    for word in new_text:
        if word.text.lower() not in stop_words and word.text.lower() not in punctuation:
            word = str(word.lemma_)
            processed_text = processed_text + " " + word

    # Perform sentiment analysis
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(processed_text)

    # Print sentiment scores and overall sentiment
    print("Sentiment Scores:")
    print("Positive:", score['pos'])
    print("Neutral:", score['neu'])
    print("Negative:", score['neg'])
    print("Compound:", score['compound'])

    # Determine overall sentiment based on compound score
    if score['compound'] >= 0.05:
        star=(score['compund']*10)%2
        return star
    elif score['compound'] <= -0.05:
        star=5-abs((score['compund']*10)%2)
        return star
    else:
        return 2.5
