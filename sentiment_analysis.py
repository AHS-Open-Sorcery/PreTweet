# Title: TextBlob: Simplified Text Processing
# Author: Steven Loria
# Version: v0.16.0.
# Date: 2020
# Availability: https://textblob.readthedocs.io/en/dev/

from textblob import TextBlob


def getSentimentPolarity(text):
    testimonial = TextBlob(text)

    # Value from -1 to 1
    return testimonial.sentiment.polarity


def printSentimentPolarity(text):
    print(getSentimentPolarity(text))


"""
# Testing code

printSentimentPolarity("")
printSentimentPolarity("like love adore")
printSentimentPolarity("dislike hate despise")
"""
