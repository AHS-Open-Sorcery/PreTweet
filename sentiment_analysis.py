# Title: TextBlob: Simplified Text Processing
# Author: Steven Loria
# Version: v0.16.0.
# Date: 2020
# Availability: https://textblob.readthedocs.io/en/dev/

from textblob import TextBlob

def printSentimentPolarity(text):
    testimonial = TextBlob(text)

    # Value from -1 to 1
    print(testimonial.sentiment.polarity)

printSentimentPolarity("")
